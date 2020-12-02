#!/usr/bin/env python3

import fileinput
import sys

expense_report = {}
for line in fileinput.input():
    entry = int(line)
    expense_report[entry] = 2020 - entry
    if expense_report[entry] in expense_report:
        print("A: ", entry * expense_report[entry])
        sys.exit(1)
