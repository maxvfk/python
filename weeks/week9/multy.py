import sys
svim=sys.version_info.major
if svim==3:
    import matplotlib.pyplot as pylab
elif svim==2:
    import pylab
    
from multiprocessing import Process, Queue, Pool
import random
def testerr (ntrials,npts,rtype,q,rd):
    print('working')
    results = [0] * ntrials
    for i in range(ntrials):
        s = 0   # sum of random points
        for j in range(npts):
            s += rd[rtype](-1,1)
        results[i] =s
    q.put(results)

def testerr2 (arg):
    ntrials,npts,rtype,rd=arg
    print('working')
    results = [0] * ntrials
    for i in range(ntrials):
        s = 0   # sum of random points
        for j in range(npts):
            s += rd[rtype](-1,1)
        results[i] =s
    return results

def testErrors(ntrials=800000,npts=100,rtype=0,process_num=8):
    rd={0:random.uniform,1:random.triangular}
    rt={0:'Uniform',1:'Triangular'}

    q = Queue()
    k=process_num
    ntrials2=ntrials//k
    pl=[0]*k
    for i in range(k):
        pl[i] = Process(target=testerr, args=(ntrials2,npts,rtype,q,rd))
        pl[i].start()
    results=[]
    for i in range(k):
        results+=q.get()    # prints "[42, None, 'hello']"
    for i in range(k):
        pl[i].join()
    # plot results in a histogram
    print(len(results))
    pylab.hist(results,bins=50)
    pylab.title('Sum of 100 random points -- {0:s} PDF ({1:,d} trials)'.format(rt[rtype],ntrials))
    pylab.xlabel('Sum')
    pylab.ylabel('Number of trials')
    pylab.show()

def testErrors2(ntrials=800000,npts=100,rtype=0,process_num=8):
    rd={0:random.uniform,1:random.triangular}
    rt={0:'Uniform',1:'Triangular'}
    with Pool(processes=process_num) as pool:
        k=process_num
        ntrials2=ntrials//k
        arg=[ntrials2,npts,rtype,rd]
        res=pool.map(testerr2,[arg]*k)
    results=[]
    for r in res:
        results+=r
   
    # plot results in a histogram
    print(len(results))

def testErrors2_7(ntrials=800000,npts=100,rtype=0,process_num=8):
    rd={0:random.uniform,1:random.triangular}
    rt={0:'Uniform',1:'Triangular'}
    pool=Pool(processes=process_num)
    k=process_num
    ntrials2=ntrials//k
    arg=[ntrials2,npts,rtype,rd]
    res=pool.map(testerr2,[arg]*k)
    results=[]
    for r in res:
        results+=r
   
    # plot results in a histogram
    print(len(results))
