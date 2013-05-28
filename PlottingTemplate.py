#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Игорь Руднев
#
# Created:     29.04.2013
# Copyright:   (c) Игорь Руднев 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
svim=sys.version_info.major
if svim==3:
    import matplotlib.pyplot as pylab
elif svim==2:
    import pylab