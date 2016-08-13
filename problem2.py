#!/usr/local/bin/python3

import sys

if __name__ ==  "__main__":
    d = {}
    text = open('problem2_text.txt', 'r')

    for j in text:
        for i in j:
            if i not in d:
                d[i] = 1
            else :
                d[i] += 1

    for j in d:
        print(j, ':', d[j])
