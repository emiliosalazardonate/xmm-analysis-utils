'''
Created on Jul 12, 2016

@author: esalazar
'''

import json
import urllib2
from math import sqrt
from astropy.coordinates import SkyCoord
from astropy import units as u
import os
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
    galacticCenterCoordinates = SkyCoord(round(float(266.416833) ,4 ),  round(float(-29.007806),4), unit=(u.degree, u.degree))
    #print ("Galactic Center %s"%(galacticCenterCoordinates))
    header = "  \\begin{table}[H] \n" \
             "  \\centering \n" \
             "  \\begin{tabular}{ccccc} \n" \
             "  \\toprule \n" \
             "  \\hline \n" \
             "  Name  & RA  & DEC & IBIS Exposure & SPI Exposure  \\\\ \n" \
             "  \\hline \n"
    print (header)
    for line in f:
          
        if line.find("2FHL_Name") == -1:
            #line = line.replace("\t\t", "\t")

            values = line.split(';', 5);
            name = values[0]
            ra = values[1]
            raFermi.append( float(ra))
            dec = values[2]
            decFermi.append(float(dec))
            err = values[3][0:5]
            url = "http://integral.esa.int/isocweb/exposureMap.html?action=query&first=%s&second=%s&exposureQuery=T&coordinates=equatorial&map=ALL_MAPS&format=json"%(ra,dec)
            try:
                #print ('%s %s %s'%(name, ra, dec))
                coordinatesFermi = SkyCoord(round(float(ra) ,4 ),  round(float(dec),4), unit=(u.degree, u.degree))
                #print (coordinatesFermi)

                #print (galacticCenterCoordinates)
                galacticCoordFermi = coordinatesFermi.transform_to('galactic')
                #print(galacticCoordFermi.b.degree)  
                #distance = coordinatesFermi.separation(galacticCenterCoordinates)

                #print ("%s (%s, %s) b=%s degrees"%(name, ra, dec,galacticCoordFermi.b.degree))
#                 if distance.degree > 10 {
#                 } else {
#                 }
                nameFermi.append(name)
                fermi[name] = [ coordinatesFermi,  round(float(err), 4)]
                response = urllib2.urlopen(url)
                data = json.load(response) 
                ibis = data.get("EXPOSURE IBIS")
                spi = data.get("EXPOSURE SPI")
                #Do not show now.
                print ("%s & %s & %s & %s & %s \\\\ \n" % (name, ra, dec, ibis, spi))

                # print "%s ibis = %s ks spi = %s ks"%(name, ibis, spi)


                fermiCount = fermiCount + 1
            except ValueError as e:
                #print e
                print "No data for %s ---------------"%(name)
#     for item in fermi.iteritems():
#         print (item)
    footer = "  \\hline \n" \
             "  \\bottomrule \n" \
             "  \\end{tabular} \n" \
             "  \\caption{INTEGRAL exposure} \n" \
             "  \\label {tab: INTEGRAL exposure}\n" \
             "\end {table}\n"
    print (footer)
    f = open("resources/INTEGRAL_CATALOG.txt")
    
    for line in f:
        srcname = line[0:24]
        ra = line[26:33]
        dec = line[34:41]
        err = line[42:46]
        #print ([ra, dec, err])
        try:
            raINTEGRAL.append(round(float(ra) ,4 ))
            decINTEGRAL.append(round(float(dec) ,4 ))
            coordinatesIntegral =  SkyCoord(round(float(ra) ,4 ),  round(float(dec),4), unit=(u.degree, u.degree))
            nameINTEGRAL.append(srcname)

            integral [srcname] =   [ coordinatesIntegral,  round(float(err)/float(60), 4)]
        except ValueError as e:
            print e
            #print "No data for %s ---------------"%(name)
    #print (fermi)
#     raFermiArray = numpy.array(raFermi)
#     decFermiArray = numpy.array(decFermi)
#     raINTEGRALArray = numpy.array(raINTEGRAL)
#     decINTEGRALArray = numpy.array(decINTEGRAL)
#     c = SkyCoord(ra=raFermiArray*u.degree, dec=decFermiArray*u.degree )  
#     catalog = SkyCoord(ra=raINTEGRALArray*u.degree, dec=decINTEGRALArray*u.degree)  
#     idx, d2d, d3d = c.match_to_catalog_sky(catalog)  
#     #print idx
#     print d2d
#     matches = catalog[idx]  
#     print matches
#     dra = (matches.ra - c.ra).arcmin
#     ddec = (matches.dec - c.dec).arcmin
#     print (dra)
#     print (ddec)
    header = "  \\begin{table}[H] \n" \
            "  \\centering \n" \
            "  \\begin{tabular}{ccccc} \n" \
            "  \\toprule \n" \
            "  \\hline \n" \
            "  Name Fermi & Name INTEGRAL  & Distance (degrees) & Radius (degrees)  \\\\ \n" \
            "  \\hline \n"
    #os.remove("resources/fermi-integral-distances.out")
    output = open("resources/fermi-integral-distances.out", 'w')

    output.write(header)

    for fermiName in fermi.iterkeys() :


         for integralName in integral.iterkeys():

             integralSource = integral[integralName][0]
             errorIntegral = integral[integralName][1]
             fermiSource = fermi[fermiName][0]
             errorFermi = fermi[fermiName][1]
             #distance = sqrt(pow((raIntegral-raFermi),2)+pow((decIntegral-decFermi) ,2))
             print (fermi[fermiName][0])
             print (integral[integralName][0])
             distance =  fermi[fermiName][0].separation( integral[integralName][0])
             print (distance)
             radio = errorFermi + errorIntegral
             #print(distance.degree)
             if distance.degree < 2:
                 output.write("%s & %s &  %s  & %s  \\\\ \n" % (
                 fermiName,integralName, distance.degree, radio))

                 print ("INTEGRAL Source Name:%s"%integralName)

                 print ("INTEGRAL Coordinates + Error (deg): %s %s %s \n"%(integralSource.ra.degree,  integralSource.dec.degree, errorIntegral))


                 print ("Fermi Source Name:%s"%fermiName)
                 print ("Fermi Coordinates + Error (deg): (%s %s) %s \n"%(fermiSource.ra.degree,  fermiSource.dec.degree, errorFermi))
                 print ('Distance %s deg > Radio %s deg\n'%(distance.degree, radio))

                 print ("------------------")
            
             if distance.degree < radio:
                 print (integralName)
                 print (integral[integralName])
                 print (fermi[fermiName])
    footer = "  \\hline \n" \
             "  \\bottomrule \n" \
             "  \\end{tabular} \n" \
             "  \\caption{Fermi-INTEGRAL distances} \n" \
             "  \\label {tab: Fermi-INTEGRAL catalogues}\n" \
             "\end {table}\n"
    output.write(footer)
