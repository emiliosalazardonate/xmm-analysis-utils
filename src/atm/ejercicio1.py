import matplotlib as matlib
import math
from blaze.expr.scalar.numbers import log10
from emcee.autocorr import function
matlib.use('TkAgg')
from astropy.io import fits
import numpy as np
import scipy
from scipy import optimize
from matplotlib.pyplot import xlabel

import matplotlib.pyplot as plt
siI = [4.48E-04,2.67E-03,0.006050771,0.010023221]   
siIT = [4000,    6000,    8000,    10000]
         
siII = [8.16E-13,1.07E-08,1.11647E-06,1.91712E-05,0.004845091]   
siIIT = [4000,    6000,    8000,    10000, 20000]
     
siIII = [3.50688E-12,8.5381E-10,3.37404E-05,0.000986668]
siIIIT = [8000,    10000, 20000, 30000]
    
siIV = [8.39653E-16,8.69521E-13, 9.32481E-07,8.67695E-05]
siIVT = [8000,    10000, 20000, 30000]


if __name__ == '__main__':
   
    siI = [4.48E-04,    1.23E-03,    4.91E-05,    4.62E-06]   
    siIT = [4000,    6000,    8000,    10000]
         
    siII = [1.12E-06,    1.83E-05,    1.03E-06]   
    siIIT = [8000,    10000, 20000]
     
    siIII = [3.51E-12, 8.54E-10, 1.41E-05, 4.78E-07]
    siIIIT = [8000,    10000, 20000, 30000]
    
    siIV = [3.90159E-29,.17068E-21,5.43421E-07,8.67275E-05]
    siIVT = [8000,    10000, 20000, 30000]
    
    plt.plot(siIT, np.log10(siI), 'r', label='SiI')
    #plt.axis([3000, 31000, 1E-016, 0.02])
    #p##3 lt.yticks(np.arange(1E-16, 0.02,1))
    line1, =plt.plot(siIIT,np.log10(siII) , 'g', label='SiII')
    line2, =plt.plot(siIIIT,np.log10(siIII) ,  'b', label='SiIII')
    
    
    plt.plot(siIVT,np.log10(siIV) ,  'y', label='SiIV')
    plt.ylabel("log10 (Nrs/Sum(Nr))" )
    plt.xlabel("Temperature (K)")
    #plt.xticks(np.arange(min(siIIIT), max(siIIIT)+1, 1.0))
    from matplotlib.legend_handler import HandlerLine2D

    #line1, = plt.plot([3,2,1], marker='o', label='Line 1')
    #line2, = plt.plot([1,2,3], marker='o', label='Line 2')
    plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})

    #plt.axis([0, 30000, 1E-16, 1])
    x = np.array(siIVT)
    y = np.array(np.log10(siIV))
    z = np.polyfit(x, y, 3)
    print z
    def f(x): return z[0] * x**3 + z[1] * x**2 + z[2]* x + z[3] 
    max_x = optimize.fmin(lambda x: -f(x), 0)
    print max_x
    plt.show()
    
    