'''
Created on Dec 19, 2016

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
      
if __name__ == '__main__':
    theta = [0.0,
            37.0,
            53.0,
            60.0,
            66.0,
            72.0,
            78.0,
            84.0]
    radians = []
    for deg in theta:
        radians.append(math.pi * deg/180)
    cosThetasMinus1 = []
    for radian in radians:
        cosThetasMinus1.append(math.cos(radian)- 1)
        
    def approxSinAtm(theta):
        return 1
      
    def ONElistmaker(n):
        listofONES = [1] * n
        return listofONES
    
    def equiRadiativo (cosThetas, k):
        equiRad = []
        for costheta in cosThetas:
            equiRad.append( 1- (1-costheta)*k)
        return equiRad
    
    
    lamba = [0.3,0.4,0.5 ,0.6 ,0.7, 0.8, 1.0,2.0,3.0,5.0,20.0]
    promedio = [1.000
                ,0.881
                ,0.757
                ,0.694
                ,0.623
                ,0.549
                ,0.471
                ,0.378
                ,0.087
                ]
    landa_08 = [1
        ,0.92
        ,0.84
        ,0.79
        ,0.74
        ,0.68
        ,0.61
        ,0.53
        ]
    x = np.array(cosThetasMinus1)
    y = np.array(landa_08)
    
    print (x)
    print (y)
    z = np.polyfit(x, y, 1)


    print (z)
    print ( approxSinAtm(theta))
    plt.scatter(x,y, label='Observations')
    line1 , = plt.plot(x, (z[0]*x + z[1]), label='Fit')
#     line2, = plt.plot(theta, cosThetas, label='Equilibrio Adiabatico')
#     line3, = plt.plot(theta, equiRadiativo(cosThetas, 0.25), label='Equilibrio Radiativo k=0.25')
#     line4, = plt.plot(theta, equiRadiativo(cosThetas, 0.5), label='Equilibrio Radiativo k=0.5')
#     line5, = plt.plot(theta, equiRadiativo(cosThetas, 0.75), label='Equilibrio Radiativo k=0.75')
#     line6, = plt.plot(theta, promedio, label='Observaciones')
#     plt.axis([ 0, 90, 0,1.05])
    plt.ylabel("I/I(0)" )
    plt.xlabel("cos(Theta)-1")
    
    from matplotlib.legend_handler import HandlerLine2D
 
    plt.legend( loc=4, handler_map={line1: HandlerLine2D(numpoints=4)}, prop={'size':8})
 
 
    plt.show()
#     import scipy.integrate as integrate
#     import scipy.special as special
#     result = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)
#     print(result)
