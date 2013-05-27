import sys
svim=sys.version_info.major
if svim==3:
    import matplotlib.pyplot as pylab
elif svim==2:
    import pylab

import string

#set line width
pylab.rcParams['lines.linewidth'] = 6
#set font size for titles
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.major.size'] = 5
#set size of numbers on y-axis
pylab.rcParams['ytick.major.size'] = 5

WORDLIST_FILENAME = "words.txt"

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

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print( "Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print ("  ", len(wordList), "words loaded.")
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vovels='eyuioa'
    vals=[]
    for word in wordList:
        numv=sum([word.count(char) for char in vovels])/float(len(word))
        vals.append(numv)

    pylab.title('Proportion of Vowels in each Word in Word List')
    pylab.xlabel('Proportion of Vowels')
    pylab.ylabel('Number of Words')
    pylab.hist(vals, bins = numBins)
    xmin,xmax = pylab.xlim()
    ymin,ymax = pylab.ylim()
    mean=float(sum(vals))/len(vals)
    sd=stdDev(vals)
    pylab.text(xmin + (xmax-xmin)*0.02,ymin+(ymax-ymin)/2,
               'Mean = ' + str(round(mean, 4))
               + '\nSD = ' + str(round(sd, 4)))

    pylab.show()

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
