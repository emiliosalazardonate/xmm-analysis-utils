import glob
import tarfile
import urllib

import os


class DownloadManager:
    def __init__(self, dataparentdirectory):
        self.URL = "http://nxsa.esac.esa.int/nxsa-sl/servlet/data-action-aio?level=ODF&obsno=%s"
        self.dataparentdirectory = dataparentdirectory
    def downloadData(self,  obsid):
        URL = self.URL % obsid
        datadirectory = "%s/%s"%(self.dataparentdirectory, obsid)
        fileODF = "%s/%s.tar.gz" % (datadirectory, obsid)

        fileODFOpener = urllib.URLopener()
        try:

            if not os.path.exists(datadirectory):
                os.makedirs(datadirectory)
            print ('\ndownloading file %s from %s' % (fileODF, URL))
            fileODFOpener.retrieve(URL, fileODF)
            print ('decompressing %s' % fileODF)

            tar = tarfile.open(fileODF)
            tar.extractall(path=datadirectory)
            tar.close()

            dataTar = glob.glob("%s/*.TAR" % (datadirectory))[0]
            tar = tarfile.open(dataTar)
            tar.extractall(path=datadirectory)
            tar.close()

        except IOError:
            print ("Not possible to access the URL %s ") % URL

    def downloadDataFromList(self,listObsId):
        for obsid in listObsId:
            self.downloadData(obsid)

    def downloadDataFromFile(self, fileName):
        file = open(fileName, 'r')
        listObsId = []
        for line in file:
            listObsId.append(line.replace("\n", ""))
        self.downloadDataFromList(listObsId)

if __name__ == '__main__':
    resourcedirectory = "/Users/esalazar/Documents/workspace/PythonUtils/science/"

    # listObsFile = "%sresources/NXSA-obsID_List-unidentifiedFermiRADEC_1513350676518.txt" % resourcedirectory
    listObsFile = "%sresources/crab.txt" % resourcedirectory

    dataParentDirectory = '%sresources/xmm-data-analisys/data/' % resourcedirectory

    downloadManager = DownloadManager(dataParentDirectory)
    downloadManager.downloadDataFromFile(listObsFile)