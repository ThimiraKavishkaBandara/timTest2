#!/usr/bin/env python3
import sys
import math

# # #Method 1, not manipulating any data in mapper
# # #TODO


#     # TODO
# count_nums = []
# res2 = {}
# curr_count = 0
# for line in sys.stdin:
#      line = line.strip()
#      word, count = line.split('\t')
#      count = int(count)
#      curr_count += count
#      count_nums.append(count)
# #print(count_nums)
# mean = int(curr_count / len(count_nums))
# s_m = curr_count
# m_n = min(count_nums)
# m_x = max(count_nums)
# v_r = int(sum(pow(x-mean,2) for x in count_nums) / len(count_nums))  # variance
# res2['Mean'] = mean
# res2['Sum'] = s_m
# res2['Min'] = m_n
# res2['Max'] = m_x
# res2['Var'] = v_r
#     # TODO
# print("res222222222222")
# print(res2)
# print('------------------------')
# #TODO
# print('%s\t%s' % (  ,  )) print as final output



#Method 2, using manipulated data from mapper
res = {}
count_nums = []
mean_count = 0
curr_count = 0
min_count = 0
max_count = 0
var_count = 0
for line in sys.stdin:
     line = line.strip()
     word, count = line.split('\t')
     count = int(count)
     if word == "Mean":
        count_nums.append(count)
        mean_count += count
        mean = mean_count / len(count_nums)
        res[word] = int(mean)
     if word == "Sum":
        curr_count += count
        s_m = curr_count
        res[word] = s_m
     if word == "Min":
        if min_count == 0:
            min_count = count
        elif count < min_count:
            min_count = count
        res[word] = min_count
     if word == "Max":
        if max_count == 0:
            max_count = count
        elif count > max_count:
            max_count = count
        res[word] = max_count
     if word == "Var":
        var_count += pow((count - mean),2)
        v_r = var_count / len(count_nums)
        v_r =int(v_r)
        res[word] = v_r

print(res)

  




#TODO
# print('%s\t%s' % (  ,  )) print as final output