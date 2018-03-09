'''
Created on Dec 22, 2016

@author: esalazar
'''
from scipy import math
import matplotlib as matlib
import math
from blaze.expr.scalar.numbers import log10
from emcee.autocorr import function
from matplotlib.mlab import frange
matlib.use('TkAgg')
from astropy.io import fits
import numpy as np

import scipy
from scipy import optimize
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlabel  
theta = [0.0,
            37.0,
            53.0,
            60.0,
            66.0,
            72.0,
            78.0,
            84.0,
            89.0]
temperaturas = [4540,
4435,
4311,
4242,
4156,
4051,
3945,
3787,
3154]

if __name__ == '__main__':
    plt.scatter(theta,temperaturas, label='Temperatures')
    #line1 , = plt.plot(x, (z[0]*x + z[1]), label='Fit')
#     line2, = plt.plot(theta, cosThetas, label='Equilibrio Adiabatico')
#     line3, = plt.plot(theta, equiRadiativo(cosThetas, 0.25), label='Equilibrio Radiativo k=0.25')
#     line4, = plt.plot(theta, equiRadiativo(cosThetas, 0.5), label='Equilibrio Radiativo k=0.5')
#     line5, = plt.plot(theta, equiRadiativo(cosThetas, 0.75), label='Equilibrio Radiativo k=0.75')
#     line6, = plt.plot(theta, promedio, label='Observaciones')
#     plt.axis([ 0, 90, 0,1.05])
    plt.ylabel("T (K)" )
    plt.xlabel("Theta")
    
    from matplotlib.legend_handler import HandlerLine2D
 
    #plt.legend( loc=4, handler_map={line1: HandlerLine2D(numpoints=4)}, prop={'size':8})
 
 
    plt.show()