#!/usr/local/bin/python3

import sys, re

if __name__ == '__main__':
    text = open('problem3_text.txt', 'r')
    i = text.read()
    result = re.findall('[a-z]+[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]+', i)

    for i in result :
        print(i)
