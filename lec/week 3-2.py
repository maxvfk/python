def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    k=0
    r=()
    for d in aTup:
        k+=1
        if k%2==1:
            r=r+(d,)
    return r

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def howMany(aDict):
    r=0
    for k in aDict.values():
        for an in k:
            r+=1
    return r
def biggest(aDict):
    if aDict!={}:
        r=aDict.keys()[0]
        i=0
        for k in aDict:
            if len(aDict[k])>i:
                r=k
                i=len(aDict[k])
        return r
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
