#!/usr/bin/env python3

import fileinput
import re

def trees( right, down ):
    counter = 0
    x = 0
    y = 0
    
    for line in fileinput.input():
        line = line.rstrip('\n')
        if y % down == 0:
            if line[x] == '#':
                counter += 1
            x = ( x + right ) % len(line)
        y += 1
    return counter

print("A: ", trees(3,1) )