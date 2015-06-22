#!/usr/bin/python
# -*- coding: UTF-8 -*-

""" Share configuration data
"""
import ConfigParser
import string, re
import logging
import sys, os

class PropertiesFileManager:
    """Read properties file and share configuration data
    """

    def readPropertiesFile(self):
        """Parse and read properties file
        and then initialize configuration data
        """
        pathname = os.path.dirname(sys.argv[0])
        #       print 'path =', pathname
        #       print 'full path =', os.path.abspath(pathname)
        self.groupesHome = os.path.abspath(pathname)
        self.propertiesFileName = self.groupesHome+"/properties/hanoi.properties"

        config = ConfigParser.ConfigParser()
        config.readfp(open(self.propertiesFileName))

            # find where is the source of file
        #self.content=config.get("path", "content")


            # mysql management
        self.mysqlhost=config.get("mysql","hostdb")
        self.mysqluser=config.get("mysql","user")
        self.mysqlpwd=config.get("mysql","pwd")
        self.mysqldbname=config.get("mysql","dbname")

        # logs management
        self.logDir = config.get("log", "logDir")
        self.logFile = self.logDir+"/hanoi.log"
        if config.get("log", "logLevel")=="DEBUG":
            self.logLevel = logging.DEBUG
        elif config.get("log", "logLevel")=="ERROR":
            self.logLevel = logging.ERROR
        else:
            self.logLevel = logging.INFO

