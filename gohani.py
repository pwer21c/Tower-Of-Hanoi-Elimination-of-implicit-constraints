#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Owner : BANG SANG HUN

"""
import sys
import logging
from ResolutionHanoiClass import ResolutionHanoi
from RuleHanoiClass import RuleHanoi
from UtilityClass import Utility

from LoggerClass import Logger
from PropertiesFileManagerClass import PropertiesFileManager
import ConfigParser
import copy
from ete2 import Tree

"""
    1. Configuration and declaration
    Read properties files from propertiesFilemanager class Declaration of logging
"""

propertiesFile = PropertiesFileManager()
propertiesFile.readPropertiesFile()
Logger.init(propertiesFile.logFile,propertiesFile.logLevel)
logger = logging.getLogger()


disk_count=int(input("How many disks ? "))

init = ResolutionHanoi(disk_count)
iDisk=init.initDisk() # initialisation n diks and 3 lods
lDisk=init.destinationDisk() #
rules = RuleHanoi(iDisk)

tree={}
treeAndValues={}
treeAndValues[1]=iDisk
treeCheck={}
treeCheck[1]=True

index=1

while not rules.isSolved(treeAndValues[index],lDisk):
    result=[]
    rules = RuleHanoi(treeAndValues[index])
    util = Utility()
    probChange = rules.canMove()
    indexitem=1
    dcopy=copy.deepcopy(treeAndValues[index])
    indexplus = util.maxNumberReturn(tree,index)

    for item in probChange:
        temp=rules.move(dcopy,item)
        if index <2 :
          treeAndValues[indexitem+indexplus]=temp
          indexitem+=1
        else :
          pp= util.findParent(tree,index,result)
          cft=True
          for item2 in pp:
              ky=tree[item2]
              if temp == treeAndValues[item2] :
                  cft=cft and False
              else:
                  cft=cft and True
              for item3 in ky:
                  if temp == treeAndValues[item3] :
                       cft = cft and False
                  else :
                       cft = cft and True
          if cft :
            treeAndValues[indexitem+indexplus]=temp
            indexitem+=1
        dcopy=copy.deepcopy(treeAndValues[index])
    tree[index]=list(range(indexplus+1,indexplus+1+(indexitem-1)))

    index+=1

#print tree
#print treeAndValues
util.printResult(tree,treeAndValues,index)


