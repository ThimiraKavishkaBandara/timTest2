#!/usr/bin/env python3
import re
import sys
import string



stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]


# TODO
with open(stopWordsPath) as f:
    
    stopWords = f.read()
    stopWords = stopWords.split()
    #print(stopWords)






#TODO 
with open(delimitersPath) as f:
 
    delimiters = f.read()
    regex = ' |\t|\,|\;|\.|\?|\!|\-|\:|\@|\[|\]|\(|\)|\{|\}|\_|\*|\/|\s|\|'





# TODO
test = []
for line in sys.stdin:
    titles = re.split(regex,line)
    for title in titles:
        title = title.lower().strip()
        if not title in stopWords:
            test.append(title)
test = [j for j in test if j]
# srt_list = sorted(test)

for word in test:
     print('%s\t%s' % (word,1))


    # print('%s\t%s' % (  ,  )) pass this output to reducer


