# -*- coding: utf-8 -*-
from array import array
from IList import IList
class ArrayList(IList):
    def __init__(self):
        self.arr = array('i', [x for x in [0]*11])
        self.siz =0
    def get( self,index ):
        return self.arr[index]
        
    def display( self ):
        for i in range(self.siz):
            print(self.arr[i])
    def size( self ):
        return self.siz
    
    def doubling(self):
        newarray =  array('i', [x for x in [0]*((self.arr.buffer_info()[1])*2)])
        for i in range(self.arr.buffer_info()[1]):
            newarray[i] = self.arr[i]
        #print(newarray)
        self.arr = newarray
        
    def add( self,e ):
        #print(self.siz)
        #print(self.arr.buffer_info()[1])
        if self.siz == self.arr.buffer_info()[1]:
            self.doubling()
        self.arr[self.siz] = e
        (self.siz) += 1
        #print(self.arr)
    
                