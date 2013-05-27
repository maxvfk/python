def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp > 0:
        if exp%2==0:
            return recurPowerNew(base**2, exp/2)
        else:
            return base*recurPowerNew(base,exp-1)
    else:
        return 1

def gcdIter(a, b):
    r=min(a,b)
    while (not((a%r==0)and(b%r==0))) and r>=1 :
        r-=1
    return r

def gcdRecur(a, b):
    if b==0:
        return a
    else:
        return gcdRecur(b, a%b)
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

def lenIter(aStr):
    d=0
    for a in aStr:
        d+=1
    return d

def lenRecur(aStr):
    if aStr=='':
        return 0
    else:
        return 1+lenRecur(aStr[1:])

def isIn(char, aStr):
    l=len(aStr)
    if l==0:
        return False
    elif aStr[l/2]==char:
        return True
    elif aStr[l/2]>char:
        return isIn(char, aStr[:l/2])
    else:
        return isIn(char, aStr[l/2+1:])
        

def semordnilap(str1, str2):
    if len(str1)==1 or len(str2)==1:
        if str1==str2:
            return True
        else:
            return False
    else:
        return semordnilap(str1[1:], str2[:-1])
    
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
def fibMetered(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)

def testFib(n):
    global numCalls
    numCalls = 0
    for i in range(n+1):
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print ('fib called ' + str(numCalls) + ' times')
