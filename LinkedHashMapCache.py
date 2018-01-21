# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 13:58:59 2017

@author: Reddy
"""
from ICache import ICache
from DoublyLinkedList import DoublyLinkedList

class LinkedHashMapCache(ICache):
    def __init__(self,capacity):
        self.__capacity = capacity
        self.__index = dict()
        self.__list = DoublyLinkedList()
    def get(self, key):
        tmp = self.__index.get(key,None)
        if(tmp == None):
            return None
        #manage LRU by brining current node to last index
        self.__list.removeAndAdd(tmp)
        return tmp.value
    def isFull(self):
        return self.__list.size() == self.__capacity
    def add(self, key,value):
        key = str(key)
        tmp = self.__index.get(key,None)
        #replace value if key exists in cache
        if(tmp != None):
            tmp.value = value
            self.__list.removeAndAdd(tmp)
        else:
            #remove LRU element if cache is full
            if(self.__list.size() == self.__capacity):
                tmp = self.__list.removeFirst()
                del self.__index[tmp.key]
            tmp = self.__list.addLast(key, value)
            self.__index[key] = tmp
    def display(self):
        self.__list.display()
    
    def capacity(self):
        return self.__capacity
    
    def  size(self):
        return self.__list.size()
    