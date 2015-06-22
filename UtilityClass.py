#!/usr/bin/python
# -*- coding: utf-8 -*-

import os.path, string, sys
import copy

class Utility :
    
      def __init__(self):
          self.indexitem=0

      def maxNumberReturn(self,tree,index):
          if index>1:
            return max(max(data for data in tree.values()))
          else :
            return index
      
      def findParent(self,tree,mypoint,result) :
          cur=self
          for item in tree.values():
              if mypoint in item :
                 key=[key for key,value in tree.iteritems() if value == item ][0]
                 if key != None :
                     result.append(key)
                 self.findParent(tree,key,result)
          return result
      
      def getParent(self,tree,mypoint,result) :
         cur=self
         for item in tree.values():
            if mypoint in item :
                key=[key for key,value in tree.iteritems() if value == item ][0]
                if key != None :
                   result.append(key)
                self.findParent(tree,key,result)
         return result

      def printResult(self,tree,treeAndValues,index) :
          result=[]
          
          printR = self.getParent(tree,len(tree)+1,result)
          printR.reverse()
          for item in printR:
             print treeAndValues[item]
          print treeAndValues[index]

      def getvalueindexitem(self):
          return self.indexitem

      def increaseindexitem(self):
          self.indexitem+=1


      def isTheSameCase(self,index,indexplus,casemove,tree,treeAndValues):
          result=[]
          if index < 2:
            return True
          else:
            listparent = self.findParent(tree,index,result)
            check=True
            for item in listparent:
               ky=tree[item]
               if casemove == treeAndValues[item]:
                    check= check and False
               else:
                    check = check and True
               for item2 in ky:
                   if casemove == treeAndValues[item2]:
                      check = check and False
                   else:
                      check = check and True
            return check



