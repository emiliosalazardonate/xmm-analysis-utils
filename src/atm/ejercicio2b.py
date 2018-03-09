'''
Created on Nov 9, 2016

@author: esalazar
'''
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
    claseI = [89.2519 ,-634.5761, 1846.1669, -2752.8323,2213.5923,-914.7857,152.5603]
    claseIII = [18.7604, -42.1636, 31.9752,-8.6640]
    claseV = [-24.1216,146.5610,-290.7332,  247.9925,-76.8249,-9.4535, 7.1944 ]
    def fI(x): return claseI[0] + claseI[1]* x + claseI[2] * x**2 +  claseI[3] * x**3 + claseI[4] * x**4 +claseI[5] * x**5 + claseI[6] * x**6
    def fIII(x): return claseIII[0] + claseIII[1]* x + claseIII[2] * x**2 +  claseIII[3] * x**3 
    def fV(x): return claseV[0] + claseV[1]* x + claseV[2] * x**2 +  claseV[3] * x**3 + claseV[4] * x**4 +claseV[5] * x**5 + claseV[6] * x**6
# 

    
    
    def Nrs_NrSrI (theta):
        return 10**(-theta*3.03)
    def Nr_Nr_1SrI(theta):
        return 10**(-fI(theta)-theta*11.03-2.5*np.log10(theta)+8.78)
    def totalSrI(theta):
        
        #return Nrs_NrSrI(theta)/(1+ Nr_Nr_1SrI(theta))
        return Nrs_NrSrI(theta)/(1 + Nr_Nr_1SrI(theta)**(-1))
    def Nrs_NrSrIII (theta):
        return 10**(-theta*3.03)
    def Nr_Nr_1SrIII(theta):
        return 10**(-fIII(theta)-theta*11.03-2.5*np.log10(theta)+8.78)
    def totalSrIII(theta):
        #return Nrs_NrSrIII(theta)/(1+ Nr_Nr_1SrIII(theta))  
     return Nrs_NrSrIII(theta)/(1 + Nr_Nr_1SrIII(theta)**(-1)) 

    def Nrs_NrSrV (theta):
        return 10**(-theta*3.03)
    def Nr_Nr_1SrV(theta):
        return 10**(-fV(theta)-theta*11.03-2.5*np.log10(theta)+8.78)
    def totalSrV(theta):
        #return Nrs_NrSrV(theta)/(1+ Nr_Nr_1SrV(theta)) 
        return Nrs_NrSrV(theta)/(1 + Nr_Nr_1SrV(theta)**(-1)) 
    
    x = frange (0.5, 1.5, 0.01) 
    xIII =    frange (0.8, 1.5, 0.01) 
    plt.title("Sr II")
    print (totalSrI(x))

    line1, = plt.plot(5040.0/x, np.log10(totalSrI(x)) , label='Clase I (Supergigantes)')
    line2, = plt.plot(5040.0/xIII, np.log10(totalSrIII(xIII)) , label='Clase III (Gigantes)')
    line3, = plt.plot(5040.0/x, np.log10(totalSrV(x)) , label='Clase V (Enanas)')
    #plt.axis([3000,12000, -07, -4.5])
    plt.ylabel("log (Nrs/Sum(Nr))" )
    plt.xlabel("Temperature (K)")

    from matplotlib.legend_handler import HandlerLine2D
 
    plt.legend( loc=4, handler_map={line1: HandlerLine2D(numpoints=4)})
 
 
    plt.show()
    
