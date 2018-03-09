import pyfits
from astropy.coordinates import SkyCoord
from astropy.utils.compat import numpy
from astropy import units as u
import numpy

from es.ucm.fis.tfm.regionfiles import RegionFileManager


class FitsFileManager:
    def __init__(self, fileName, regionFile, source):
        self.hdulist = pyfits.open(fileName)
        self.regionFile = regionFile
        self.regionFile.createHeader()
        self.source = source

    def read(self):
        tabdata = self.hdulist[1].data
        # 0782170201
        # J0826.1-4500;126.529;-45.000;0.041;unk
        # coordinatesFermi = SkyCoord(126.529, -45.000, unit=(u.degree, u.degree))
        # errorFermi = 0.041
        # regionFile.addLine('circle(126.529,-45,147.600") # text={J0826.1-4500}\n')

        # 0606420101:
        # ;J1834.6 - 0701 278.651;-7.018;0.047;
        # J1837.4-0717;279.363;-7.296;0.036 J1837.6-0717
        # J1839.5-0705;279.876;-7.084;0.084;


        #coordinatesFermi = SkyCoord(279.363, -7.296, unit=(u.degree, u.degree))
        coordinatesFermi = self.source.coord
        errorFermi = self.source.error

        self.regionFile.addLine('circle(279.363,-7.296,%s") # text={J1837.4-0717}\n' % (errorFermi * 3600))

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
                self.regionFile.addLine(
                    'circle(%s,%s,%s") # color=blue font="helvetica 8 normal" text={d = %ssigma}\n' % (
                    ra, dec, tabdata[i]['RADEC_ERR'], round(float(sigma), 4)))
            self.regionFile.addLine('circle(126.529,-45,147.600") # text={J0826.1-4500}\n')
        self.regionFile.close()

if __name__ == '__main__':

    instrument = 'pn'
    resourcedirectory = "/Users/esalazar/Documents/workspace/PythonUtils/science/"
    obsid = "0606420101"

    dataParentDirectory = '%sresources/xmm-data-analisys/data/' % resourcedirectory
    analysisParentDirectory = '%sresources/xmm-data-analisys/analysis/' % resourcedirectory
    analysisdirectory = "%s/%s/"%(analysisParentDirectory, obsid)
    regionFile = RegionFileManager("%s/test.reg"%analysisdirectory)
    fitsManager = FitsFileManager('%s/%s/%s_emllist.fits'
                                  % (analysisdirectory, instrument, instrument), regionFile)
    fitsManager.read()