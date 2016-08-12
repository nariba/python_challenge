#!/usr/local/bin/python3

import sys

text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.\n"

if __name__ ==  "__main__":
    for i in text:
        if ord(i) >= 65 and ord(i) <= 90 :
            if ord(i) + 2 > 90 :
                sys.stdout.write(chr(ord(i) + 2 - 26))
            else :
                sys.stdout.write(chr(ord(i) + 2))
        elif ord(i) >= 97 and ord(i) <= 122 :
            if ord(i) + 2 > 122 :
                sys.stdout.write(chr(ord(i) + 2 - 26))
            else :
                sys.stdout.write(chr(ord(i) + 2))

        else :
            sys.stdout.write(chr(ord(i)))
