#!/usr/local/bin/python3

import sys, pickle

if __name__ == '__main__':
    with open('problem5_text.txt', mode='rb') as f:
        text = pickle.load(f)
    for line in text:
        print(''.join(elmt[0] * elmt[1] for elmt in line))
