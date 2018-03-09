import urllib2


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
    # galacticCenterCoordinates = SkyCoord(round(float(266.416833) ,4 ),  round(float(-29.007806),4), unit=(u.degree, u.degree))
    # print ("Galactic Center %s"%(galacticCenterCoordinates))

    for line in f:

        if line.find("2FHL_Name") == -1:
            values = line.split(';', 5);
            name = values[0]
            ra = values[1]
            raFermi.append(float(ra))
            dec = values[2]
            decFermi.append(float(dec))
            err = values[3][0:5]
            link = "http://nxsa.esac.esa.int/nxsa-web/#pos=%s,%s&size=0.007,0.006&entity=EPIC_PPS_SOURCES"%(ra, dec)
            #link = "http://nxsa.esac.esa.int/nxsa-web/#pos=204.25829,-29.86576&size=0.007,0.006&entity=EPIC_PPS_SOURCES"
            print (link)
            response = urllib2.urlopen(link)
            html = response.read()
            # if "table" in response:
            print (response.read())
