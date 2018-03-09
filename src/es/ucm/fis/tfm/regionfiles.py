import numpy
import pyfits
from astropy.coordinates import SkyCoord
from astropy import units as u


class RegionFileManager:
    def __init__(self, fileName):
        print ("reg file to be created in %s" %fileName)
        self.file = open(fileName, 'w')

    def createHeader(self):
        self.file.write("# Region file format: DS9 version 4.1\n")
        self.file.write('global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\n')
        self.file.write("fk5\n")
    def addLine(self, line):
        self.file.write(line)
    def close(self):
        self.file.close()

if __name__ == '__main__':
    instrument = 'pn'
    resourcedirectory = "/Users/esalazar/Documents/workspace/PythonUtils/science/"
    obsid = "0606420101"

    dataParentDirectory = '%sresources/xmm-data-analisys/data/' % resourcedirectory
    analysisParentDirectory = '%sresources/xmm-data-analisys/analysis/' % resourcedirectory
    analysisdirectory = "%s/%s/"%(analysisParentDirectory, obsid)
    regionFile = RegionFileManager("%s/%s/test.reg"%(analysisdirectory, instrument))
    regionFile.createHeader()
    fileName= '%s/%s/%s_emllist.fits'% (analysisdirectory, instrument, instrument)
    hdulist = pyfits.open(fileName)
    tabdata = hdulist[1].data
    # 0782170201
    # J0826.1-4500;126.529;-45.000;0.041;unk
    # coordinatesFermi = SkyCoord(126.529, -45.000, unit=(u.degree, u.degree))
    # errorFermi = 0.041
    # regionFile.addLine('circle(126.529,-45,147.600") # text={J0826.1-4500}\n')

    # 0606420101:
    # ;J1834.6 - 0701 278.651;-7.018;0.047;
    # J1837.4-0717;279.363;-7.296;0.036 J1837.6-0717
    # J1839.5-0705;279.876;-7.084;0.084;


    coordinatesFermi = SkyCoord(279.363, -7.296, unit=(u.degree, u.degree))
    errorFermi = 0.036

    regionFile.addLine('circle(279.363,-7.296,%s") # text={J1837.4-0717}\n' % (errorFermi * 3600))

    for i in range(0, len(tabdata)):
        instrumentCode = {0: 'Summary', 1: 'PN', 2: 'MOS1', 3: 'MOS2'}
        instrumentId = tabdata[i]['ID_INST']
        instrument = instrumentCode[instrumentId]
        errorXMM = tabdata[i]['RADEC_ERR'] / 3600
        if instrumentId == 0:
            ra = tabdata[i]['RA']
            dec = tabdata[i]['DEC']
            errorXMM = tabdata[i]['RADEC_ERR'] / 3600
            det_ml = tabdata[i]['DET_ML']
            # print('%s-%s-%s (%s,%s,%s) %s ' % (tabdata[i]['ML_ID_SRC'], tabdata[i]['BOX_ID_SRC'], instrument,
            # ra, dec, tabdata[i]['RADEC_ERR'], tabdata[i]['DET_ML']))
            coordinatesXMM = SkyCoord(ra, dec, unit=(u.degree, u.degree))
            distance = coordinatesFermi.separation(coordinatesXMM)
            denominator = numpy.sqrt(numpy.power(errorFermi * 3600, 2) + 4)
            sigma = (distance.degree * 3600) / denominator
            print ("(%s, %s) d=%ssigma <-> d = %sdeg errorXMM = %s det_ml=%s " % (
                ra, dec, sigma, distance.degree, errorXMM, det_ml))
            regionFile.addLine(
                'circle(%s,%s,%s") # color=blue font="helvetica 8 normal" text={d = %ssigma}\n' % (
                    ra, dec, tabdata[i]['RADEC_ERR'], round(float(sigma), 4)))
        regionFile.addLine('circle(126.529,-45,147.600") # text={J0826.1-4500}\n')
    regionFile.close()

