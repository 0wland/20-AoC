#!/usr/bin/env python3

import fileinput
import re

valid = 0
report = {}
for line in fileinput.input():
    data = re.split("[-: \n]", line.rstrip('\n'))
    first = int(data[0])-1
    second = int(data[1])-1
    passwd = data[4]
    if second <= len(passwd):
        if  ( passwd[first] == data[2] and passwd[second] != data[2] ) or \
            ( passwd[first] != data[2] and passwd[second] == data[2] ):
            valid += 1

print("B: ", valid)