#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MAX
#
# Created:     11.04.2013
# Copyright:   (c) MAX 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def stdDev(L):
    if len(L)!=0:
        mean=float(sum(L))/len(L)

        dev=0.0
        for l in L:
            dev+=(float(mean)-l)**2

        dev=(float(dev)/float(len(L)))**0.5
        return dev
    return float('NaN')


def stdDevOfLengths(L):
    lofs=[len(l) for l in L]
    return stdDev(lofs)

def stdVar(L):
    return stdDev(L)/(float(sum(L))/len(L))