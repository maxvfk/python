class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    def __eq__(self, notself):
        return (self.getX()==notself.getX()) and (self.getY()==notself.getY())

class Queue(object):
    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self,val):
        self.vals.insert(0,val)

    def remove (self):
        try:
            return self.vals.pop()
        except : raise ValueError
def genPrimes():
    plist=[2]
    yield 2

    while True:
        x=plist[-1]+1
        while sum([int((x%p)==0) for p in plist])!=0: x+=1
        yield x
        plist.append(x)

class hashSet(object):
    def __init__(self, numBuckets):
        if type(numBuckets)!=int:
            raise ValueError('Value should be an integer')
        elif numBuckets<=0:
            raise ValueError('Value should be greater than zero')
        self.buks={i:[] for i in range(numBuckets)}
        self.bnum=numBuckets

    def hashValue(self, e):
        if type(e)!=int:
            raise ValueError('Value should be an integer')
        return e%self.bnum

    def member(self, e):
        return self.buks[self.hashValue(e)].count(e)>0

    def insert(self,e):
        if not self.member(e):
            self.buks[self.hashValue(e)].append(e)


    def remove(self,e):
        try:
            self.buks[self.hashValue(e)].remove(e)
        except:
            raise ValueError

    def getNumBuckets(self):
        return self.bnum

    def __str__(self):
        return '\n'.join([(str(k)+':  '+str(self.buks[k])) for k in self.buks.keys()])


def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

class imn(object):
    def __init__(self):
        self.sn=0

    def setv(self,e):
        self.sn=e

    def isMyNumber(self,guess):

        if guess == self.sn:
            return 0
        elif guess < self.sn:
            return -1
        else:
            return 1

def jumpAndBackpedal(isMyNumber):
    guess = 0
    while True:
        sign = isMyNumber(guess)
        if sign == 0:
            return guess
        elif sign == -1:
            guess += 1
        else:
            guess -= 1

def generateForm(story, listOfAdjs, listOfNouns, listOfVerbs):
    lofl2=['[ADJ]','[NOUN]','[VERB]']
    lofl1=[listOfAdjs, listOfNouns, listOfVerbs]
    story2=story
    for i in range(3):
        for w in lofl1[i]:
            story2=story2.replace(w,lofl2[i])
    return story2

def generateTemplates(madLibsForm):
    s=madLibsForm
    l=[]
    while True:
        i=s.find('[')
        if i==-1:
            break
        s=s[i:]
        i=s.find(']')
        s2=s[:i+1]
        if s2 in ['[ADJ]','[NOUN]','[VERB]']:
            l.append(s[:i+1])
        s=s[(i+1):]
    return l

def verifyWord(userWord, madTemplate, listOfAdjs, listOfNouns, listOfVerbs):
    d={'[ADJ]':listOfAdjs,'[VERB]':listOfVerbs,'[NOUN]':listOfNouns}
    return userWord in d[madTemplate]

story = 'The ravenous zombies started attacking yesterday'
listOfAdjs = ['ravenous']
listOfNouns = ['zombies', 'humans', 'yesterday']
listOfVerbs = ['attacking', 'attacks']



#print story

s=generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)
#print s
#print generateTemplates(s)
vvv=verifyWord('attacks', '[VERB]', listOfAdjs, listOfNouns, listOfVerbs)
print (vvv)
story = 'At the creepy thrift store I found a pair of plaid pants that looked like something your grandpa might wear'
listOfAdjs = ['creepy', 'plaid']
listOfNouns = ['store', 'pants', 'something', 'grandpa']
listOfVerbs = ['found', 'looked']

s=generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)
print (s)
print (generateTemplates(s))



def numPens(n):

    def np(a,b,c,n):
        k=5*a+8*b+24*c
        if k==n:
           return True
        if k<n:
            return np(a+1,b,c,n) or np(a,b+1,c,n) or np(a,b,c+1,n)
        else:
            return False

    return np(0,0,0,n)

a=5
b=6
c=5
d=1
n=5*a+8*b+24*c+d
def itt():
    n=1
    while n<100:
        yield [n,numPens(n)]
        n+=1

for i in itt():
    print (i)
print (numPens(n))

print (map(numPens,[5,8,24,29,37,45,23,84,13]))
nnnn=input('asdf')