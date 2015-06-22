import os.path, string, sys
import logging, re

from PropertiesFileManagerClass import PropertiesFileManager
import ConfigParser
import datetime,time

propertiesFile = PropertiesFileManager()
propertiesFile.readPropertiesFile()

class ResolutionHanoi :

      def __init__(self,disk_number):
           self.logger = logging.getLogger()
           self.disk_number = disk_number
           self.logger.info("disknummber : " + str(disk_number))

      def initDisk(self):
           disk=list(range(self.disk_number))
           disk_arrange=list(map(lambda x: x+1,disk))
           matrix_peg_disk = [disk_arrange,[],[]]
           return matrix_peg_disk
 
      def destinationDisk(self):
           diskl=list(range(self.disk_number))
           disk_arrangel=list(map(lambda x: x+1,diskl))
           matrix_peg_diskl = [[],[],disk_arrangel]
           return matrix_peg_diskl
                      
