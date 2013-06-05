#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Игорь Руднев
#
# Created:     03.06.2013
# Copyright:   (c) Игорь Руднев 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.
    """
    if newFrob.myName()<atMe.myName():
        newMe=atMe.getBefore()
        if newMe==None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        else:
            if newFrob.myName()>newMe.myName():
                atMe.setBefore(newFrob)
                newFrob.setAfter(atMe)
                newMe.setAfter(newFrob)
                newFrob.setBefore(newMe)
            else:
                insert(newMe, newFrob)



    else:
        newMe=atMe.getAfter()
        if newMe==None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        else:
            if newFrob.myName()<newMe.myName():
                atMe.setAfter(newFrob)
                newFrob.setBefore(atMe)
                newMe.setBefore(newFrob)
                newFrob.setAfter(newMe)
            else:
                insert(newMe, newFrob)



def findFront(start):

    bb=start.getBefore()
    if bb==None:
        return start
    else:
        return  findFront(bb)

def prgr(xa):
    def prb(xa):
        if xa!=None:
            b=xa.getBefore()

            if b!=None:
                prb(b)
                print b.myName()
    def pra(xa):
        if xa!=None:
            b=xa.getAfter()
            if b!=None:

                print b.myName()
                pra(b)
    prb(xa)
    print xa.myName()
    pra(xa)





eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)

aa=Frob('aa')
bb=Frob('bb')
cc=Frob('cc')
dd=Frob('dd')
ee=Frob('ee')
ff=Frob('ff')
gg=Frob('gg')
hh=Frob('hh')
ii=Frob('ii')
jj=Frob('jj')
kk=Frob('kk')
ll=Frob('ll')
mm=Frob('mm')

insert(gg,ii)
print findFront(ii).name
insert(gg,kk)
print findFront(ii).name
insert(gg,cc)
print findFront(ii).name
insert(gg,bb)
insert(gg,aa)
print findFront(ii).name
