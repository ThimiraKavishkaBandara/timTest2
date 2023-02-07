#!/usr/bin/env python3
import sys
count_nums = []
op_list = ["Mean", "Sum","Min", "Max", "Var"]
res = {}
curr_count = 0
for line in sys.stdin:
     line = line.strip()
     word, count = line.split('\t')
     count_nums.append(count)
res = {}   
for ol in op_list:
    res[ol]=count_nums

for key,val in res.items():
    for v in val:
        print('%s\t%s' % (key,v )) 


    # print('%s\t%s' % (  ,  )) pass this output to reducer
