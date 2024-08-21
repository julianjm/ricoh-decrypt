import sys
import hashlib
import Crypto.Cipher.AES
import Crypto.Util.Padding
import csv


class AESRicoh:
    """
    Decrypts Ricoh AES encrypted strings.

    The encryption is AES-256-CBC with a key derived from the passphrase using SHA-256.
    The IV is the first 16 bytes of the key.
    """

    def __init__(self, passphrase):
        self.AESKEY = hashlib.sha256(passphrase.encode()).digest()
        self.IV = self.AESKEY[:16]

    def decrypt(self, msg):
        ct = bytes.fromhex(msg)
        cipher = Crypto.Cipher.AES.new(
            self.AESKEY, Crypto.Cipher.AES.MODE_CBC, iv=self.IV)
        pt = cipher.decrypt(ct)
        pt = Crypto.Util.Padding.unpad(pt, 16)
        return pt.decode()

    @staticmethod
    def sanity_check():
        aestmp = AESRicoh("1234abcd")
        pttmp = aestmp.decrypt(
            "a725a525e800529b6319abea0ceab19241ea052cf9685833cd23c94e9428c6accab6db0ef2136cea09b312dd13abbc7ad43ef3594bc72b721e5a9b04542ffda626f8a2fc7ce95514adf27b86c4e21e3fa6c60aa7e89bcaf88675793e5b5d126f")
        assert pttmp == "System Settings - Display/Input - Key/Keyboard/Input Assistance - Key Repeat - Key Repeat", "Sanity check failed"
        del aestmp, pttmp


AESRicoh.sanity_check()

if len(sys.argv) != 4:
    print("Usage: %s <passphrase> <encryptedcsv|-> <outputfile|->" %
          sys.argv[0])
    exit(1)

passphrase = sys.argv[1]
filename = sys.argv[2]
outputfile = sys.argv[3]


aes = AESRicoh(passphrase)

if filename == "-":
    inputf = sys.stdin
else:
    inputf = open(filename, "r")
reader = csv.reader(inputf)

if outputfile == "-":
    outputf = sys.stdout
else:
    outputf = open(outputfile, "w")
writer = csv.writer(outputf)

csv.field_size_limit(sys.maxsize)
for row in reader:
    for i in range(len(row)):
        try:
            row[i] = aes.decrypt(row[i])
        except Exception as ex:
            pass
    writer.writerow(row)

inputf.close()
outputf.close()
