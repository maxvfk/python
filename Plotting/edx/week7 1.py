#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      MAX
#
# Created:     02.04.2013
# Copyright:   (c) MAX 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
svim=sys.version_info.major
if svim==3:
    import matplotlib.pyplot as pylab
elif svim==2:
    import pylab


lines = open('julyTemps.txt', 'r').readlines()

fields=[line.split(' ') for line in lines]

nfields =[[int(field[0]),int(field[1]),int(field[2])] for field in fields if len(field) == 3 and field[0].isdigit()]
days=[field[0] for field in nfields]
defs=[field[1]-field[2] for field in nfields]
mint=[(field[2]-32.0)*(5.0/9.0) for field in nfields]
maxt=[(field[1]-32.0)*(5.0/9.0) for field in nfields]
avgt=[(b+a)/2 for a,b in zip(mint,maxt)]
print (zip(days,defs))

pylab.figure(1)
pylab.plot(days,maxt,'r-o',label='maximum temperature')
pylab.plot(days,avgt,'g-d',label='average temperature')
pylab.plot(days,mint,'b-^',label='minimum temperature')
xmin,xmax = pylab.xlim()
ymin,ymax = pylab.ylim()

pylab.title('Day by Day Temperature in Boston in July 2012')
pylab.xlabel('Days')
pylab.ylabel('Temperature in Celsius')
pylab.legend()

#pylab.text(xmin + (xmax-xmin)*0.02, ymin+(ymax-ymin)/2.0,'Mean = ')
pylab.savefig('L12_P5_graph',dpi=200)


#pylab.rcParams
pylab.show()
