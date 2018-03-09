'''
Created on Sep 15, 2017

@author: esalazar
'''

import json
import urllib2
from math import sqrt
from astropy.coordinates import SkyCoord
from astropy import units as u
import numpy
import math
if __name__ == '__main__':
    
    f = open("resources/sourcesFermi.out")
    fermi = {}
    integral = {}
    raFermi = []
    decFermi = []
    nameFermi = []
    raINTEGRAL = []
    decINTEGRAL = []
    nameINTEGRAL = []
    fermiCount = 0
    #galacticCenterCoordinates = SkyCoord(round(float(266.416833) ,4 ),  round(float(-29.007806),4), unit=(u.degree, u.degree))
    #print ("Galactic Center %s"%(galacticCenterCoordinates))

    for line in f:
          
        if line.find("2FHL_Name") == -1:
            values = line.split(';', 5);
            name = values[0]
            ra = values[1]
            raFermi.append( float(ra))
            dec = values[2]
            decFermi.append(float(dec))
            err = values[3][0:5]
            try:
                #print ('%s %s %s'%(name, ra, dec))
                coordinatesFermi = SkyCoord(round(float(ra) ,4 ),  round(float(dec),4), unit=(u.degree, u.degree))
                galacticCoordFermi = coordinatesFermi.transform_to('galactic')
                #print "" 
                
                if abs(galacticCoordFermi.b.degree)> 10:
                    #print ("%s (%s, %s) b=%s degrees"%(name, ra, dec,galacticCoordFermi.b.degree))
                    #print "%s %s @desc@ %s"%(ra, dec, name)
                    print "%s %s %s"%(ra, dec, name)
                    
#                 if distance.degree > 10 {
#                 } else {
#                 }
                nameFermi.append(name)
                fermi[name] = [ coordinatesFermi,  round(float(err), 4)]
                fermiCount = fermiCount + 1
            except ValueError as e:
                #print e
                print "No data for %s ---------------"%(name)