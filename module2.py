#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MAX
#
# Created:     27.04.2013
# Copyright:   (c) MAX 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math

Pe=10**(-6)

def MVal(S,Pe=10**(-6)):
    SNR=10**(S/10)
    return math.log2(1-(3/2)*SNR/math.log(Pe))

Ml=[MVal(S) for S in [24,32,42,30]]


SNR=20
W=6
C=W*math.log2(1+SNR)

print('C:',C)

def Perr(G):
 return 0.01-0.5*math.erfc((G/20)/(2.0**0.5))

def finder(f,minlim=0,maxlim=1000.0,pres=0.00000000001,res=0):
    return finder2(f,minlim,maxlim,pres,res)

def finder2(f,minlim,maxlim,pres,res):
    p=(maxlim+minlim)/2
    ans=f(p)
    print(ans)
    if abs(ans-res)<pres:
        return p
    if ans>res:
        return finder2(f,minlim,p,pres,res)
    else:
        return finder2(f,p,maxlim,pres,res)

def lagrange(k,t,N):
    ans=1
    for i in range(-N,N+1):
        if i!=k: ans*=(t-i)/(k-i)
    return ans

class LagrangeInt(object):
    def __init__(self,seq):
        ind=len(seq)//2
        dictseq={(i-ind):seq[i] for i in range(len(seq))}
        self.seq=dictseq


    def getIntVal(self,t,N):
        return sum((self.seq[k])*lagrange(-k,t,N) for k in range(-N,N+1))

seq=[0,0,-4, 4,-2,-3,3,0,0]

tl=[1/4,0,1/2,-1/4]
Nl=[1,4,2,2]

L=LagrangeInt(seq)
f= lambda tl,Nl: [L.getIntVal(t,N) for t,N in zip(tl,Nl)]
print(f(tl,Nl))