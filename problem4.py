#!/usr/local/bin/python3

import sys
from urllib.request import urlopen
import re

if __name__ == '__main__':
    response = urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
    #response = urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022")
    #response = urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579")
    while True:

        html = response.read()
        print(html)

        ans = re.findall('[0-9]{1,5}', str(html))
        print(str(ans[0]))
        response = urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(ans[0]))
