import os

from es.ucm.fis.tfm.datamodel import Source
from es.ucm.fis.tfm.datareduction import DataReductionManager
from es.ucm.fis.tfm.imagegenerator import ImageManager
from es.ucm.fis.tfm.xmmdownload import DownloadManager


if __name__ == '__main__':


    resourcedirectory = "/Users/esalazar/Documents/workspace/PythonUtils/science/"

    #listObsFile = "%sresources/NXSA-obsID_List-unidentifiedFermiRADEC_1513350676518.txt" % resourcedirectory
    #listObsFile = "%sresources/crab.txt" % resourcedirectory
    SAS_DIR = "/Applications/sas_16.1.0-Darwin-15.6.0-64/xmmsas_20170719_1539"
    SAS_CCFPATH ="/Users/esalazar/xmm-data-analisys/ccf/"

    os.environ['SAS_DIR'] = SAS_DIR
    os.environ['SAS_CCFPATH'] = SAS_CCFPATH

    dataParentDirectory = '%sresources/xmm-data-analisys/data/test/' % resourcedirectory
    analysisParentDirectory = '%sresources/xmm-data-analisys/analysis/test/' % resourcedirectory
    obsid = "0782170201"

    downloadManager = DownloadManager(dataParentDirectory)
    downloadManager.downloadData(obsid)


    dataReductionManager = DataReductionManager(dataParentDirectory,analysisParentDirectory)
    dataReductionManager.createScientificProducts(obsid)


    source = Source ("J0826.1-4500", 126.529,-45.000,0.041)
    rateLimit = 1
    imageManager = ImageManager("%s/%s/"%(analysisParentDirectory,obsid) , 'pn', source, rateLimit)

    imageManager.createImage()

