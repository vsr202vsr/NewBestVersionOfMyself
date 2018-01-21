# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:35:47 2017

@author: Reddy
"""
from ListNode import ListNode
class TestLinkedList(object):
    def addFirst(self,head=None,e=None):
        tmp = ListNode(e)
        tmp.next = head.next
        head.next = tmp
    def getLastNode(self,head):
        current = head.next
        while(current.next!=None):
            current=current.next
        return current
    def display( self,head ):
        current = head.next
        while(current!= None):
            print(current.data,"-->", end='')
            current = current.next