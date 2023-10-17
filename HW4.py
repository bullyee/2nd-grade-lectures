'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Information Security Homework 4
Brute Force partially known AES cipherkey
author: https://github.com/bullyee
date: 2023/10/16 23:27
requires package: Cryptodome
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
from Crypto.Cipher import AES
import base64

#change these for your own ciphertext & key!!!!!
data = '89NEvN56VtNjo1w5x3whmFUOZOqTaRyoMnIrPjCGKUv5n7kgGFHDmStzEgDFAU7QnZOK9MLeO/FW4etzIOhpKfOsw5xSD4Em72X1O2FRfaM='
key = '2 ? mYD;@ ;x v"i'

keyarr = bytearray(key,"utf8")
#substitute btyes in key for the unknown bytes
#33~126 are the most used chars in utf8
for a in range(33,127):
    for b in range(33,127):
        for c in range (33,127):
            for d in range(33,127):
                keyarr[1] = a
                keyarr[3] = b
                keyarr[9] = c
                keyarr[12] = d
                keybytes = bytes(keyarr)
                cipher = AES.new(keybytes.ljust(16,b'\0'), AES.MODE_ECB)
                cipheredData = cipher.decrypt(base64.b64decode(data))
                try:
                    #solution must be able to be decoded with utf8
                    print(f"key:{keybytes} plaintext:{cipheredData.decode('utf8')}")
                except:
                    continue
