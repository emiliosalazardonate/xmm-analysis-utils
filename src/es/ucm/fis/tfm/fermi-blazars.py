'''
Created on Nov 27, 2017

@author: esalazar
'''
from decimal import Decimal

import os

if __name__ == '__main__':
    f = open("resources/fermin-all-sources.txt")
    os.remove("resources/fermi-all-sources-discriminated.out")
    output = open("resources/fermi-all-sources-discriminated.out", 'w')
    os.remove("resources/fermi-all-sources-discriminated.out2")
    output2 = open("resources/fermi-all-sources-discriminated.out2", 'w')
    count = 0
    for line in f:
        #print line
        if  ( line.find("bll") > -1) or ( line.find("fsrq") > -1)or ( line.find("bcu") > -1): 
            #print line
            name, ra, dec, type = line.split(",")
            ra = ra.replace ('"', "")
            ra= ra.replace (' ', "")
            dec = dec.replace ('"', "")
            dec= dec.replace (' ', "")
            ra = Decimal(ra)
            dec  = Decimal(dec)
            name = name.replace ('"', "")
            #print ("%s, %s, %s"%(ra, dec, name))
            print ("%s, %s %s"%(ra, dec, name))

            #output.write("%s, %s %s \n"%(ra, dec, name))
            count = count +1
            if (count<640):
                output.write("%s,%s\n" % (ra, dec))
            else:
                output2.write("%s,%s\n" % (ra, dec))

        else:
            name, ra, dec, type = line.split(",")
            ra = ra.replace ('"', "")
            ra= ra.replace (' ', "")
            dec = dec.replace ('"', "")
            dec= dec.replace (' ', "")
            ra = Decimal(ra)
            dec  = Decimal(dec)
            name = name.replace ('"', "")
            type = type.replace ('"', "")
            type = type.replace ('\n', "")

            #print ("%s, %s, %s"%(ra, dec, name))
            #print ("[%s, %s %s class '%s']"%(ra, dec, name, type))
            #output.write("[%s, %s %s class '%s']\n"%(ra, dec, name, type))

    print " Total number of blazars %s"%count   