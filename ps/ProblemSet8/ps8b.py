# Problem Set 8: Simulating the Spread of Disease and Virus Population Dynamics

import numpy
import random
import sys
svim=sys.version_info.major
if svim==3:
    import matplotlib.pyplot as pylab
elif svim==2:
    import pylab
'''
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 2
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.birthProb=maxBirthProb
        self.clProb=clearProb

        # TODO

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.birthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        # TODO
        return self.clProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step.
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """

        # TODO
        return random.random()<float(self.clProb)



    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.getMaxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        # TODO
        if random.random()<(self.getMaxBirthProb() * (float(1) - popDensity)):
            newVirus=SimpleVirus(self.birthProb,self.clProb)
            return newVirus
        raise NoChildException

class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        self.viruses=viruses
        self.maxPop=maxPop
        # TODO

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        # TODO
        return self.viruses

    def getMaxPop(self):
        """
        Returns the max population.
        """
        # TODO
        return self.maxPop

    def getTotalPop(self):
        """
        Gets the size of the current total virus population.
        returns: The total virus population (an integer)
        """
        return len(self.viruses)
        # TODO


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.

        - The current population density is calculated. This population density
          value is used until the next call to update()

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.

        returns: The total virus population at the end of the update (an
        integer)
        """
        popden=float(self.getTotalPop())/float(self.maxPop)

        for vir in self.getViruses()[:]:
            if vir.doesClear(): self.viruses.remove(vir)

        for vir in self.viruses[:]:
            try:
                self.viruses.append(vir.reproduce(popden))
            except NoChildException:
                pass

        return self.getTotalPop()
        # TODO



#
# PROBLEM 3
#
def simulationWithoutDrug(numViruses=100, maxPop=1000, maxBirthProb=0.1,
                         clearProb=0.05, numTrials=10):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """

    # TODO
    time=range(300)
    popSize=[0 for t in time]
    for trials in range(numTrials):
        viruses=[SimpleVirus(maxBirthProb,clearProb) for numv in range(numViruses)]
        patient=Patient(viruses,maxPop)
        for t in time:
            popSize[t]+=patient.update()
    popSizeAvg=[float(popSize[t])/float(numTrials) for t in time]




    pylab.figure(1)
    pylab.plot(time,popSizeAvg,'r-o',label='Virus Population')

    pylab.title('SimpleVirus simulation')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Average Virus Population')
    pylab.legend()
    pylab.show()
    #return popSizeAvg

#
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """

        # TODO
        SimpleVirus.__init__(self,maxBirthProb,clearProb)
        self.mutProb=mutProb
        self.res=resistances

    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        # TODO
        return self.res

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        # TODO
        return self.mutProb
    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """

        # TODO
        return self.res.get(drug,False)


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:

        self.getMaxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb, clearProb, and mutProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        # TODO
        ans=True
        for drug in activeDrugs:
            ans=ans and self.isResistantTo(drug)

        if ans and (random.random()<(self.getMaxBirthProb()*(1.0-popDensity))):
            res1=self.getResistances()
            res2=res1.copy()
            for dr in res2:
                if random.random()<self.mutProb:
                    res2[dr]=not res2[dr]
            newVirus=ResistantVirus(self.getMaxBirthProb(),self.getClearProb(),res2,self.mutProb)
            return newVirus
        raise NoChildException


class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """

        # TODO
        Patient.__init__(self,viruses,maxPop)
        self.drugs=[]

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """

        # TODO
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.drugs

        # TODO


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        vlist=self.getViruses()
        pop=0
        for vir in vlist:
            ans=sum([int(not vir.isResistantTo(drug)) for drug in drugResist])
            if ans==0: pop+=1
        return pop


        # TODO


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """

        # TODO


        for vir in self.getViruses()[:]:
            if vir.doesClear(): self.viruses.remove(vir)

        popden=float(self.getTotalPop())/float(self.maxPop)

        for vir in self.viruses[:]:
            try:
                self.viruses.append(vir.reproduce(popden,self.getPrescriptions()))
            except NoChildException:
                pass

        return self.getTotalPop()


#
# PROBLEM 5
#
def simulationWithDrug2(numViruses=100, maxPop=1000, maxBirthProb=0.1, clearProb=0.05,
      resistances={'d1': False,'d2':False,'d3':False},mutProb=0.005, numTrials=10):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1).
    numTrials: number of simulation runs to execute (an integer)

    """

    # TODO
    time=range(150)
    time2=range(150,200)
    time3=range(200,300)
    time4=range(300,1000)
    otime=time+time2+time3+time4
    popSize=[0 for t in otime]
    popSizeRes=popSize[:]
    for trials in range(numTrials):
        viruses=[ResistantVirus(maxBirthProb,clearProb,resistances,mutProb )
                                   for numv in range(numViruses)]
        patient=TreatedPatient(viruses,maxPop)
        for t in time:
            popSize[t]+=patient.update()
            popSizeRes[t]+=patient.getResistPop(['d1'])
        patient.addPrescription('d1')
       # patient.addPrescription('d2')
       # patient.addPrescription('d3')
        for t in time2:
            popSize[t]+=patient.update()
            popSizeRes[t]+=patient.getResistPop(['d1'])
        patient.addPrescription('d2')
        for t in time3:
            popSize[t]+=patient.update()
            popSizeRes[t]+=patient.getResistPop(['d1'])
        #patient.addPrescription('d3')
        for t in time4:
            popSize[t]+=patient.update()
            popSizeRes[t]+=patient.getResistPop(['d1'])


    popSizeAvg=[float(popSize[t])/float(numTrials) for t in otime]
    popSizeResAvg=[float(popSizeRes[t])/float(numTrials) for t in otime]



    pylab.figure(1)
    pylab.plot(otime,popSizeAvg,'b-',label='total virus population')
    pylab.plot(otime,popSizeResAvg,'r-',label='resistant virus population')
    pylab.title('ResistantVirus simulation')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Average Virus Population')
    pylab.legend()
    pylab.show()


def simulationWithDrug(numViruses=100, maxPop=1000, maxBirthProb=0.1, clearProb=0.05,
      resistances={'guttagonol': False, 'grimpex': False},
      mutProb=0.005, numTrials=100,timelist=[150,150,150]):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1).
    numTrials: number of simulation runs to execute (an integer)

    """

    # TODO
    time_axis=range(sum(timelist))
    popSize=[0 for t in time_axis]
    popSizeRes=popSize[:]
    popHist=[]
    for trials in range(numTrials):
        viruses=[ResistantVirus(maxBirthProb,clearProb,resistances,mutProb )
                                   for numv in range(numViruses)]
        patient=TreatedPatient(viruses,maxPop)
        t0=0
        for num,time in enumerate(timelist):
            t1=time+t0
            for t in range(t0,t1):
                temp=patient.update()
                popSize[t]+=temp
                popSizeRes[t]+=patient.getResistPop(patient.getPrescriptions())
            patient.addPrescription(list(resistances)[num%(len(timelist)-1)])
            t0=t1
        popHist.append(temp)
        print('Delay: {:d}, Trial{:d}'.format(timelist[1],trials+1))
    popSizeAvg=[float(popSize[t])/float(numTrials) for t in time_axis]
    popSizeResAvg=[float(popSizeRes[t])/float(numTrials) for t in time_axis]


    pylab.figure('avg')
    pylab.plot(time_axis,popSizeAvg,'b-',label='total virus population')
    pylab.plot(time_axis,popSizeResAvg,'r-',label='resistant virus population')
    pylab.title('ResistantVirus simulation, {:d} Trials'.format(numTrials))
    pylab.xlabel('Time Steps')
    pylab.ylabel('Average Virus Population')
    pylab.legend()
    return popHist
##    pylab.figure('hist')
##    pylab.hist(popHist,bins=50)
##    pylab.title(str(len(popHist)))

##    return popSizeAvg[-1]

