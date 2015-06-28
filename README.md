# grado_informatica_criptografia
A repo hosting all the assigment and source code of the Cryptography subject. ETSIIT

## Example of P3/Ej7. Sign files with RSA

Here is the help:

```bash
usage: ej7.py [-h] -d <path> [-g <key size>] [-s <file> <priv key>]
              [-v <original file> <signed file> <pub key>]

Generate RSA keys, sign and verify signed files

optional arguments:
  -h, --help            show this help message and exit
  -d <path>, --directory <path>
                        Where to store the keys and signature
  -g <key size>, --genkeys <key size>
                        Generate RSA keys
  -s <file> <priv key>, --sign <file> <priv key>
                        Sign a file
  -v <original file> <signed file> <pub key>, --verify <original file> <signed file> <pub key>
                        Verify a signed file
```

Once downloaded, you can generate your keys with:

```bash
$ python ./ej7.py -d ./ -g 2048
```

And you will see something like this:

```bash
Generating keys...
Done, keys placed in ./
Your public key:
NjY4NzMzOTk2NDY3NDM0OTg0MjI1NTExOTU5NDE4NTE0OTA0MzIyNDgyNDYzODk0NDQzOTM0NzA0OTc4MjEzMzUzMDMwMjA4MTc0Nzg4ODA1N........

Your private key:
NTM0OTg3MTk3MTczOTQ3OTg3MzgwNDA5NTY3NTM0ODExOTIzNDU3OTg1OTcxMTE1NTU1MTQ3NzYzOTgyNTcwNjgyNDI0MTY2NTM5ODMxMDQ0M........
```

Once you have your public and private key, in the path you choose, you can sign a file with:

```bash
$ python ./ej7.py -d ./ -s file.txt rsa.priv
```

The output would be:

```bash
Signing file...
Sign placed in ./file.txt.signed here is the sign
MjAyMzMzNDcyNDA2MDE2NDMzODE5NTU2NjE4MjkwMjg3NzkzMDM4NzE0MTE.......................
```

Finally, to check that a file was signed correctly:

```bash
$ python ./ej7.py -d ./ -v file.txt file.txt.signed rsa.pub

Verifying signature...
File is correctly signed
Original signature: 
6489173261045097199711934183582747376698259832904786118783303916308307801147620581729652089220119753020693094141877657507765409178638893860418373696327180
Current signature 
6489173261045097199711934183582747376698259832904786118783303916308307801147620581729652089220119753020693094141877657507765409178638893860418373696327180
```

If the file was corrupted, when the above command is executed, you will see:

```bash
Verifying signature...

##########################
## INVALID SIGNATURE!!! ##
##########################

Original signature: 
6091672226240801698371810859476188289341568805009997190131273579330832769362617745024212278025102239097390392429061669931887332626496467275750968867723954
Current signature 
6489173261045097199711934183582747376698259832904786118783303916308307801147620581729652089220119753020693094141877657507765409178638893860418373696327180
```


