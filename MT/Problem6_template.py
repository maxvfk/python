import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30

def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    global MAXRABBITPOP
    global CURRENTRABBITPOP
    c=range(CURRENTRABBITPOP)
    for rab in c:
        if random.random()>(CURRENTRABBITPOP/float(MAXRABBITPOP)):
            CURRENTRABBITPOP+=1

    # Your code here
    pass

def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # Your code here
    global MAXRABBITPOP
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    c=range(CURRENTFOXPOP)
    for fox in c:
        if random.random()<(CURRENTRABBITPOP/float(MAXRABBITPOP)) and (CURRENTRABBITPOP>10):
            if CURRENTRABBITPOP>10: CURRENTRABBITPOP-=1
            if (random.random()<1.0/3.0): CURRENTFOXPOP+=1
        else:
            if (random.random()>0.1) and (CURRENTFOXPOP>10): CURRENTFOXPOP-=1



    pass

def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    foxlist , rablist=[], []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rablist.append(CURRENTRABBITPOP)
        foxlist.append(CURRENTFOXPOP)
    # Your code here
    return (rablist,foxlist)


(rablist,foxlist)=runSimulation(200)

coeff = pylab.polyfit(range(len(rablist)), rablist, 2)

pylab.plot(pylab.polyval(coeff, range(len(rablist))),'g',label='rabbit curve')

pylab.plot(rablist,'b',label='rabbit')
pylab.plot(foxlist,'r',label='fox')
pylab.legend()
pylab.show()


