#!/usr/bin/env python3

import fileinput
import sys

report = {}
for line in fileinput.input():
    first = int(line)
    report[first] = 2020 - first

    for second in report:
        third = report[first] - second
        if third in report:
            print("B: ", first * second * third )
            sys.exit(1)
