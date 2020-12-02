#!/usr/bin/env python3

import fileinput
import re

valid = 0
report = {}
for line in fileinput.input():
    count = 0
    data = re.split("[-: \n]", line.rstrip('\n'))
    for char in data[4]:
        if data[2] == char:
            count += 1
    if int(data[0]) <= count and count <= int(data[1]):
        valid += 1

print("A: ", valid)