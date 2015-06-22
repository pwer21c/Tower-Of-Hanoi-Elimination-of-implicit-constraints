#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path, string, sys
import logging, re
import copy


from PropertiesFileManagerClass import PropertiesFileManager
import ConfigParser
import datetime,time
from ete2 import Tree

propertiesFile = PropertiesFileManager()
propertiesFile.readPropertiesFile()


class RuleHanoi :

      def __init__(self,disk_now):
           self.logger = logging.getLogger()
           self.t=Tree()
           self.res=[]
           self.res2={}
           self.disk=disk_now
           

      def but(self):
           pass

      def canMove(self):
          """
          """
          res1=[]
          index1=0
          for items in self.disk:
              if len(items) !=0 :
                   check=items[0]
                   index2=0
                   for items2 in self.disk:
                      if ( len(items2) !=0 and check < items2[0]) or (len(items2)==0):
                         res1.append((index1,index2))
                      index2+=1
              index1+=1
          return res1

      def move(self,disknow,case):
          temp=[]
          take_value=disknow[case[0]][0]
          for item in range(len(disknow)):
            temp.append(disknow[item])
      
          temp[case[0]].remove(take_value)
          temp[case[1]].insert(0,take_value)
          return temp
            
      def maxNumberReturn(self,tree):
          return max(data[0] for data in tree.values())
      
      def findParent(tree,mypoint,result) :
          for item in tree.values():
              if mypoint in item :
                 key=[key for key,value in tree.iteritems() if value == item ][0]
                 if key != None :
                     result.append(key)
                 findParent(tree,key,result)
          return result
      

      def isSolved(self,disk,disk_last):
          return (len(disk[0]) == 0 and \
                 len(disk[1]) == 0 and \
                 len(disk[2]) == 3 and disk == disk_last )


