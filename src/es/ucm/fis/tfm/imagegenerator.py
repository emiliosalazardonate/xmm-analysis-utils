import os

from es.ucm.fis.tfm.regionfiles import RegionFileManager
from es.ucm.fis.tfm.xmmfits import FitsFileManager
import subprocess


class ImageManager:
    def __init__(self, analysisdirectory, instrument,ratecut = 1):
        self.instrument = instrument
        self.analysisdirectory = analysisdirectory
        self.ratecut = ratecut

        print ("%s  ==== " %analysisdirectory)
    def createImage(self) :
        analysisdirectory = self.analysisdirectory
        instrument = self.instrument
        os.environ['DATRED'] = '%s/%s' % (analysisdirectory, instrument)
        os.environ['PATH'] = '%s:/Applications/ds9.darwinelcapitan.7.5/' % os.environ['PATH']
        if instrument == 'pn':
            self.createPNImages(analysisdirectory, instrument)
            self.detectSources(analysisdirectory, instrument)
            self.createRegionFile(analysisdirectory, instrument)

            print ("------------------")
            scrdisplaycommand = "srcdisplay boxlistset=pn_emllist.fits imageset=pn_image_full.fits "
            print ("/////////////////")
            print (scrdisplaycommand)
            p = subprocess.Popen(scrdisplaycommand, shell=True, cwd='%s/%s' % (analysisdirectory, instrument))
            p.wait()
            print ("------------------")

    def createRegionFile(self,analysisdirectory, instrument):
        regionFile = RegionFileManager('%s/%s/automatic-region.reg' % (analysisdirectory, instrument))
        fitsManager = FitsFileManager('%s/%s/%s_emllist.fits' % (analysisdirectory, instrument, instrument), regionFile)
        fitsManager.read()


    def createPNImages(self,analysisdirectory, instrument):
        eventFile = "$DATRED/PN.event"
        lightcurvefile = "pn_back_lightc.fits"
        tabgtigenfile = "pn_back_gti.fits"
        fullimagefile = "pn_image_full.fits"
        os.environ['DATRED'] = '%s/%s' % (analysisdirectory, instrument)

        evselectcommand = "evselect table=%s " \
                          "expression='#XMMEA_EP&&(PI>10000)&&(PATTERN==0)' " \
                          "rateset='%s' " \
                          "timebinsize=10" \
                          " withrateset=yes " \
                          "maketimecolumn=yes makeratecolumn=yes" % (eventFile, lightcurvefile)
        print ("/////////////////")
        print (evselectcommand)
        print ('%s/%s' % (analysisdirectory, instrument))
        p = subprocess.Popen(evselectcommand, shell=True, cwd='%s/%s' % (analysisdirectory, instrument))
        p.wait()
        print ("-----------------")

        tabgtigencommand = "tabgtigen table=%s expression='RATE<%s'  gtiset=%s" % (lightcurvefile, self.ratecut, tabgtigenfile)
        print ("/////////////////")
        print (tabgtigencommand)
        p = subprocess.Popen(tabgtigencommand, shell=True, cwd='%s/%s' % (analysisdirectory, instrument))
        p.wait()
        print ("-----------------")
        self.createImagesInEnergyRanges(analysisdirectory, instrument, eventFile, fullimagefile, tabgtigenfile, 300, 12000)
        self.createImagesInEnergyRanges(analysisdirectory, instrument, eventFile, 'pn_image_b1.fits', tabgtigenfile, 300, 500)
        self.createImagesInEnergyRanges(analysisdirectory, instrument, eventFile, 'pn_image_b2.fits', tabgtigenfile, 500, 1000)
        self.createImagesInEnergyRanges(analysisdirectory, instrument, eventFile, 'pn_image_b3.fits', tabgtigenfile, 1000, 2000)
        self.createImagesInEnergyRanges(analysisdirectory, instrument, eventFile, 'pn_image_b4.fits', tabgtigenfile, 2000, 4500)
        self.createImagesInEnergyRanges(analysisdirectory, instrument, eventFile, 'pn_image_b5.fits', tabgtigenfile, 4500, 12000)


    def detectSources(self,analysisdirectory, instrument):
        edetect_chaincommand = "edetect_chain imagesets='\"pn_image_b1.fits\" \"pn_image_b2.fits\" \"pn_image_b3.fits\" \"pn_image_b4.fits\" \"pn_image_b5.fits\"' " \
                               "eventsets=$DATRED/PN.event attitudeset=$DATRED/AttHk.ds " \
                               "pimin='300 500 1000 2000 4500' pimax='500 1000 2000 4500 12000' " \
                               "ecf='9.525 8.121 5.867 1.953 0.578' " \
                               "eboxl_list='pn_eboxlist_l.fits' eboxm_list='pn_eboxlist_m.fits' " \
                               "esp_nsplinenodes=16 eml_list='pn_emllist.fits' esen_mlmin=5 "

        print ("////////edetect_chaincommand/////////")
        print (edetect_chaincommand)
        p = subprocess.Popen(edetect_chaincommand, shell=True, cwd='%s/%s' % (analysisdirectory, instrument))
        p.wait()
    def createImagesInEnergyRanges(self,analysisdirectory, instrument, eventFile, imagefile, tabgtigenfile, minPI, maxPI):
        evselectcommand = "evselect table=%s:EVENTS imagebinning='binSize' imageset='%s'" \
                          " withimageset=yes xcolumn='X' ycolumn='Y' ximagebinsize=40 yimagebinsize=40 " \
                          " expression='#XMMEA_EP&&(PI in [%s:%s])&&(PATTERN in [0:4])&&(FLAG==0) " \
                          "&& gti(%s,TIME)'" % (eventFile, imagefile,
                                                minPI, maxPI, tabgtigenfile)

        print ("//////createImagesInEnergyRanges///////////")
        print (evselectcommand)
        p = subprocess.Popen(evselectcommand, shell=True, cwd='%s/%s' % (analysisdirectory, instrument))
        p.wait()
        print ("------createImagesInEnergyRanges--------")
if __name__ == '__main__':


    resourcedirectory = "/Users/esalazar/Documents/workspace/PythonUtils/science/"
    dataParentDirectory = '%sresources/xmm-data-analisys/data/' % resourcedirectory
    analysisParentDirectory = '%sresources/xmm-data-analisys/analysis/' % resourcedirectory
    obsid = "0606420101"
    imageManager = ImageManager("%s/%s/"%(analysisParentDirectory,obsid) , 'pn')
    imageManager.createImage()




