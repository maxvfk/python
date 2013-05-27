#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Игорь Руднев
#
# Created:     03.04.2013
# Copyright:   (c) Игорь Руднев 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
svim=sys.version_info.major
if svim==3:
    import matplotlib.pyplot as pylab
elif svim==2:
    import pylab

import random
random.randint(1, 5)

print random.choice(['apple', 'banana', 'cat'])

def genEven():
    def getev(n):
        evl=[2]
        for i in range(3,n+1):
            ans=True
            for ev in evl[:]:
                ans=ans and i%ev!=0
            if ans:
                evl.append(i)
        return evl
    return random.choice(getev(100))


def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1

def doran(n):
    ddd=[dist2() for i in range(n)]
    zerr=[random.random() for i in range(len(ddd))]

    pylab.figure(1)
    pylab.plot(ddd,zerr,'o',linestyle='None')
    pylab.show()
