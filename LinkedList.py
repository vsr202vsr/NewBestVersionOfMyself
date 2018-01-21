# -*- coding: utf-8 -*-
from IList import IList
class ListNode( object ):
    def __init__(self,data=None):
        self.data = 0
        if data:
            self.data = data
        self.next = None

class LinkedList(IList):
    def __init__(self):
        self.head = ListNode()
        self.last = self.head
        self.siz = 0
    def get( self,index ):
        return None
        
    def display( self ):
        current = ListNode()
        current = self.head.next
        for i in range(self.siz):
            if current is not None:
                print(current.data)
                current = current.next
    def size( self ):
        return self.siz
    
            
    def add( self,e ):
        temp = ListNode(e)
        self.last.next= temp
        self.last=temp
        (self.siz) += 1
       

