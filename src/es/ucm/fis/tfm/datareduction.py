import glob
import os
import subprocess

import sys


class DataReductionManager:
    def __init__(self, datadirectory, analysisdirectory):
        self.datadirectory = datadirectory
        self.analysisdirectory = analysisdirectory

    def createScientificProducts(self, obsid):
        try:
            datadirectory = "%s/%s" % (self.datadirectory, obsid)
            analysisdirectory = "%s/%s" % (self.analysisdirectory, obsid)

            print (datadirectory)
            print (analysisdirectory)
            if not os.path.exists(analysisdirectory):
                os.makedirs(analysisdirectory)

            os.environ['SAS_ODF'] = datadirectory

            p = subprocess.Popen(['cifbuild'], cwd=datadirectory)
            p.wait()

            os.environ['SAS_CCF'] = "%s/ccf.cif" % datadirectory

            p = subprocess.Popen(['odfingest'], cwd=datadirectory)
            p.wait()

            sasodf = glob.glob("%s/*SCX00000SUM.SAS" % (datadirectory))[0]
            os.environ['SAS_ODF'] = sasodf
            print (sasodf)
            print ("start xmmextractor")
            p = subprocess.Popen(['xmmextractor'], cwd=analysisdirectory)
            p.wait()
            print ("finished xmmextractor")
            for instrument in ['pn', 'mos']:
                self.createSymbolicLinks(analysisdirectory, instrument)
        except:
            print ("ERROR------------------------Problem with analyzing %s" % obsid)
            print("Unexpected error:", sys.exc_info()[0])


    def createScientificProductsFromList(self,listObsId):
        for obsid in listObsId:
            self.createScientificProducts(obsid)

    def createScientificProductsFromFile(self, fileName):
        file = open(fileName, 'r')
        listObsId = []
        for line in file:
            listObsId.append(line.replace("\n", ""))
        self.createScientificProductsFromList(listObsId)

    def createSymbolicLink(self,filelist, link):
        if len(filelist) > 0:
            file = filelist[0]
            if not os.path.exists(link):
                os.symlink(file, link)
                print ("created symbolyc link: %s %s" % (file, link))
            else:
                print ("the symbolyc link: %s already exists" % (link))

    def createSymbolicLinks(self,analysisdirectory, instrument):
        try:
            attHkdsFile = glob.glob("%s/%s/*AttHk.ds*" % (analysisdirectory, instrument))
            self.createSymbolicLink(attHkdsFile, "%s/%s/AttHk.ds" % (analysisdirectory, instrument))
            if instrument == 'pn':
                eventsFile = glob.glob("%s/%s/*ImagingEvts.ds" % (analysisdirectory, instrument))
                self.createSymbolicLink(eventsFile, "%s/%s/PN.event" % (analysisdirectory, instrument))
            elif instrument == 'mos':
                eventsFile = glob.glob("%s/%s/*EMOS1*ImagingEvts.ds" % (analysisdirectory, instrument))
                self.createSymbolicLink(eventsFile, "%s/%s/MOS1.event" % (analysisdirectory, instrument))

                eventsFile = glob.glob("%s/%s/*EMOS2*ImagingEvts.ds" % (analysisdirectory, instrument))
                self.createSymbolicLink(eventsFile, "%s/%s/MOS2.event" % (analysisdirectory, instrument))
        except:
            print ("Problem when generating symbolic links")


if __name__ == '__main__':
    resourcedirectory = "/Users/esalazar/Documents/workspace/PythonUtils/science/"

    dataParentDirectory = '%sresources/xmm-data-analisys/data/' % resourcedirectory
    analysisParentDirectory = '%sresources/xmm-data-analisys/analysis/' % resourcedirectory

    dataReductionManager = DataReductionManager(dataParentDirectory,analysisParentDirectory)
    dataReductionManager.createScientificProducts("0135730701")