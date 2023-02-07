#!/usr/bin/env python3
import sys


# TODO

res = []
alist = []
for line in sys.stdin:
       line = line.strip()
       word, count = line.split('\t',1)
#        res.append(word, count)

# sorted_res = sorted()

#TODO
       print('%s\t%s' % (word , count)) 


