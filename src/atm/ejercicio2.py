'''
Created on Nov 6, 2016

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
#     x = frange (0.4, 1.6, 0.01)
#     line1, = plt.plot(x, fI(x) , label='Clase I')
#     line2, = plt.plot(x, fIII(x),  label='Clase III')
#     line3, = plt.plot(x, fV(x)  , label='Clase V')
# 
#     plt.ylabel("logPe" )
#     plt.xlabel(r'$\theta (5040/T)$')
#     #plt.xticks(np.arange(min(siIIIT), max(siIIIT)+1, 1.0))
#     from matplotlib.legend_handler import HandlerLine2D
# 
#     plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
# 
# 
#     plt.show()
#10^(-D35-$B35*7,87-2,5*LOG10($B35)+8,78)
    #Nr,s/Nr        

    
    
    def Nrs_NrFeI (theta):
        return 10**(-theta*4.53)
    def Nr_Nr_1FeI(theta):
        return 10**(-fI(theta)-theta*7.87-2.5*np.log10(theta)+8.78)
    def totalFeI(theta):
        return Nrs_NrFeI(theta)/(1+ Nr_Nr_1FeI(theta))
    
    def Nrs_NrFeIII (theta):
        return 10**(-theta*4.53)
    def Nr_Nr_1FeIII(theta):
        return 10**(-fIII(theta)-theta*7.87-2.5*np.log10(theta)+8.78)
    def totalFeIII(theta):
        return Nrs_NrFeIII(theta)/(1+ Nr_Nr_1FeIII(theta))   

    def Nrs_NrFeV (theta):
        return 10**(-theta*4.53)
    def Nr_Nr_1FeV(theta):
        return 10**(-fV(theta)-theta*7.87-2.5*np.log10(theta)+8.78)
    def totalFeV(theta):
        return Nrs_NrFeV(theta)/(1+ Nr_Nr_1FeV(theta)) 
       
    x = frange (0.5, 1.5, 0.01) 
    xIII =    frange (0.8, 1.5, 0.01) 
    plt.title("Fe I")
    print (5040.0/x)

    line1, = plt.plot(5040.0/x, np.log10(totalFeI(x)) , label='Clase I (Supergigantes)')
    line2, = plt.plot(5040.0/xIII, np.log10(totalFeIII(xIII)) , label='Clase III (Gigantes)')
    line3, = plt.plot(5040.0/x, np.log10(totalFeV(x)) , label='Clase V (Enanas)')
    plt.axis([3000,12000, -07, -4.5])
    plt.ylabel("log (Nrs/Sum(Nr))" )
    plt.xlabel("Temperature (K)")

    from matplotlib.legend_handler import HandlerLine2D
 
    plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
 
 
    plt.show()
    
    