# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b import *

#
# PROBLEM 1
#
def simulationDelayedTreatment(numTrials=10):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    for num,time in enumerate(time_list):
        pylab.subplot(2,2,num+1)
        simsimulationWithDrug(numTrials=numTrials, timeBefore=time)
##    pylab.title('ResistantVirus simulation')
    # TODO






#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
