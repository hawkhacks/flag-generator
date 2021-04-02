#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import random
import math
import secrets
import string

char_map = [
        ['a', '4', '@'],
        ['b', '8'],
        ['c'],
        ['d'],
        ['e', '3'],
        ['f'],
        ['g', '6', '9'],
        ['h'],
        ['i', '1'],
        ['j'],
        ['k'],
        ['l', '1'],
        ['m'],
        ['n'],
        ['o', '0'],
        ['p'],
        ['q'],
        ['r'],
        ['s', '5', '$'],
        ['t', '7'],
        ['u'],
        ['v'],
        ['w'],
        ['x'],
        ['y'],
        ['z', '2'],
    ]

def change(c):
    if c.isalpha():
        c = c.lower()
        char_set = char_map[ord(c) - ord('a')]
        new_c = char_set[random.randint(0, len(char_set) - 1)]
        return new_c, (c == new_c) * math.log2(len(char_set))
    else:
        return c, 0

def main():
    global args
    chars = string.ascii_lowercase + string.digits
    parser = argparse.ArgumentParser()
    parser.add_argument("string", help = "origin flag string")
    args = parser.parse_args()
    entropy = 0
    print('hawkHacks{', end='')
    for c in args.string.replace(' ', '_'):
        new_c, e = change(c)
        print(new_c, end = '')
        entropy += e
    print('_' + ''.join(secrets.choice(chars) for i in range(16)) + '}')
    print(f"Added entropy: {entropy:.2f} bits")

if __name__ == "__main__":
    main()
