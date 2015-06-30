# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:02:41 2015

@author: Alejandro Alcalde (elbauldelprogramador.com)
"""

import sys
sys.path.append('../../P1')

import random
import binascii
import argparse

from hashlib import sha512

import Utils
from modularArith.ej2 import moduloInverse
from modularArith.ej3 import powerModInt

PATH = "/tmp/"
PUB_KEY = PATH + "rsa.pub"
PRIV_KEY = PATH + "rsa.priv"
SIGNED_FILE = PATH + "signed.bin"

def main():
    parser = argparse.ArgumentParser(description='Generate RSA keys, sign and verify signed files')
    parser.add_argument('-d','--directory', help='Where to store the keys and signature', type=str, metavar='<path>', required=True)
    parser.add_argument('-g','--genkeys', help='Generate RSA keys', type=int, metavar='<key size>')
    parser.add_argument('-s', '--sign', help='Sign a file', type=str, nargs=2, metavar=('<file>', '<priv key>'))
    parser.add_argument('-v', '--verify', help='Verify a signed file', type=str, nargs=3, metavar=('<original file>', '<signed file>', '<pub key>'))

    args = parser.parse_args()

    if args.genkeys == None and args.sign == None and args.verify == None:
        parser.print_help()
    else:
        global PATH
        global PUB_KEY
        global PRIV_KEY
        global SIGNED_FILE

        PATH = args.directory
        PUB_KEY = PATH + "rsa.pub"
        PRIV_KEY = PATH + "rsa.priv"

        if args.genkeys:
            print "Generating " + str(args.genkeys) + " bit keys..."
            gen_keys(args.genkeys)
            print "Done, keys placed in " + PATH
            print "Your public key:"
            Utils.ascii_print(PUB_KEY)
            print "Your private key:"
            Utils.ascii_print(PRIV_KEY)
        elif args.sign:
            print "Signing file..."
            SIGNED_FILE = PATH + args.sign[0] + ".signed"
            sign(args.sign[0], args.sign[1])
            print "Sign placed in " + SIGNED_FILE + " here is the sign"
            Utils.ascii_print(SIGNED_FILE)
        elif args.verify:
            print "Verifying signature..."
            check, original = verify_sign(args.verify[0], args.verify[1], args.verify[2])
            if check == original:
                print "File is correctly signed"
            else:
                warning = "## INVALID SIGNATURE!!! ##"
                print
                print "#"*len(warning)
                print warning
                print "#"*len(warning)
                print
            print "Original signature: \n" + str(original)
            print "Current signature \n" + str(check)

def gen_keys(size=1024):
    """Generate a RSA key pair of the given size bytes.
    :param size: Size in bits of the keys (Default is 1024 bits)
    """
    size >>= 1
    # Get two random numbers of a fixed bits size
    print "Real size %d" % size
    n1,n2 = random.getrandbits(size), random.getrandbits(size)

    p = Utils.get_prime(n1)
    q = Utils.get_prime(n2)

    n = p * q
    phi_n = (p-1)*(q-1)
    e = Utils.compute_e(phi_n)
    # Compute the private key, d = e^-1 mod (phi_n)
    d = moduloInverse(e, phi_n)

    ascii_n = binascii.b2a_base64(str(n))
    with open(PUB_KEY, 'wb') as file:
        ascii_e = binascii.b2a_base64(str(e))
        file.write(ascii_n)
        file.write(ascii_e)
    with open(PRIV_KEY, 'wb') as file:
        ascii_d = binascii.b2a_base64(str(d))
        file.write(ascii_d)
        file.write(ascii_n)

def sign(input_file=None, priv_key=None):
    """Sign the given file with a private key
    :param input_file: The file to sign
    :param priv_key: The private RSA key to use when signing the file
    :returns: A Signature placed in a file in PATH
    """

    if input_file == None or priv_key == None:
        print "You must enter a file to sign and a private key"
        exit
    else:
        with open(priv_key, 'rb') as file:
            d = int(binascii.a2b_base64(file.readline()))
            n = int(binascii.a2b_base64(file.readline()))
        with open(input_file, 'rb') as file:
            h = int(sha512(file.read()).hexdigest(),16)

        with open(SIGNED_FILE, 'wb') as file:
            ascii_sign = binascii.b2a_base64(str(powerModInt(h, d, n)))
            file.write(ascii_sign)

def verify_sign(original_file=None, signature=None, pub_key=None):
    """Verify that a signature is valid, given the original signed file, the signature
    and the public key.

    :param original_file: The file which was signed
    :param signature: The signature made when the file was signed
    :pub_key: The RSA public key to verify that the file was signed correctly
    :returns: The current signature and the original
    """
    if original_file == None or signature == None or pub_key == None:
      print "You must enter a file, signed file and a public key"
      exit
    else:
        with open(pub_key, 'rb') as file:
            n = int(binascii.a2b_base64(file.readline()))
            e = int(binascii.a2b_base64(file.readline()))
        with open(signature, 'rb') as file:
            sign = int(binascii.a2b_base64(file.readline()))

        with open(original_file, 'rb') as file:
            original = int(sha512(file.read()).hexdigest(), 16) % n

        return powerModInt(sign, e, n), original

if __name__ == '__main__':
    main()
