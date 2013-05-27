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

def memoize(f):
    def memf(*x):
        if x not in memf.cache:
            memf.cache[x]=f(*x)
        return memf.cache[x]
    memf.cache = {}
    return memf

def memoize2(f):
    def memf(*x):
        y=(tuple(i) for i in x)

        if y not in memf.cache:
            memf.cache[y]=f(*x)
        return memf.cache[y]
    memf.cache = {}
    return memf