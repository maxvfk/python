#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MAX
#
# Created:     18.05.2013
# Copyright:   (c) MAX 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import string
import numpy as np
import matplotlib.pyplot as plt

lines = open('words.txt', 'r').read()
words=lines.split()
print(len(words))
lets=string.ascii_lowercase

num=[0 for let in lets ]
nums=[num[:] for ind in range(3)]
for ind,let in enumerate(lets):

    for word in words:
        times=(word.count(let))
        if times!=0:
            if times>3: times=3
            nums[times-1][ind]+=1




N = 5
menMeans   = [20, 35, 30, 35, 27]
womenMeans = (25, 32, 34, 20, 25)
menStd     = (2, 3, 4, 1, 2)
womenStd   = (3, 5, 2, 3, 3)
ind = np.arange(len(lets))    # the x locations for the groups
width = 0.5       # the width of the bars: can also be len(x) sequence

##p1 = plt.bar(ind, [k1+k2+k3 for k1,k2,k3 in zip(nums[0],nums[1],nums[2])],align='center', width=0.95, color='y')
p2 = plt.bar(ind, nums[0],align='center',   width=0.8, color='r')
p3 = plt.bar(ind, nums[1],align='center', width=0.7, color='g', bottom=nums[0])
p4 = plt.bar(ind, nums[2],align='center', width=0.6, color='b', bottom=[k1+k2 for k1,k2 in zip(nums[0],nums[1])])




##
plt.xlabel('Letter')
plt.ylabel('Number of words')
plt.title('Number of words in words.txt by letter occured in the word')
plt.xticks(ind, (list(lets)) )
##plt.yticks(np.arange(0,81,10))
plt.legend( (p2[0], p3[0],p4[0]), ('Letter occured once', 'Letter occured twice', 'Letter occured three \n or more times') )

plt.show()