# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 13:35:44 2017

@author: Reddy
"""
from DListNode import DListNode
class DoublyLinkedList(object):
    def __init__(self):
        self.__head = DListNode()
        self.__size = 0
        
    def removeAndAdd(self,current):
#		//unlink node from list
        current.prev.next = current.next
        current.next.prev = current.prev
#		//attach node at end
        current.prev = self.__head.prev
        current.next = self.__head
        self.__head.prev.next = current
        self.__head.prev = current
        
    def addLast(self, key,value):
         tmp = DListNode(key,value)
         tmp.prev = self.__head.prev
         tmp.next = self.__head
         self.__head.prev.next = tmp
         self.__head.prev = tmp
         self.__size+=1
         return tmp
          
    def display(self):
        current =DListNode()
        current = self.__head.next
        for i in range(self.__size):
            if current is not None:
                print(str(current.key) + ":" + str(current.value))
                current = current.next
    
    def size(self):
        return self.__size
    
    def removeFirst(self):
        tmp = self.__head.next
        tmp.next.prev = self.__head
        self.__head.next = tmp.next
        self.__size -=1
        return tmp
  
	