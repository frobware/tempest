#!/usr/bin/env python

import sys
import argparse
import datetime

parser = argparse.ArgumentParser(description='Copy standard input, emitting progress complete.')
parser.add_argument('--print-date', help='prepend current date and time', action='store_true', required=False)
parser.add_argument('--nlines', type=int, help='expected number of lines in input', required=False)
args = parser.parse_args()

nlines = 0.0

while 1:
    line = sys.stdin.readline()
    if not line:
        break
    if not args.nlines:
        print line,
        continue
    nlines = nlines + 1
    if args.print_date:
        now = datetime.datetime.now()
        print now.strftime("%Y-%m-%d %H:%M:%S"),
    print "{:3.0f}% {}".format(nlines / args.nlines * 100.0, line),
