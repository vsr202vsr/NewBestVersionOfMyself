# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 16:48:47 2017

@author: Reddy
"""
import time

class RandonGenerator(object):
    __A,__B,__M=5,7,1024
    
    def __init__(self,seed=None):
        self.seed= int(time.time())*45289647896
        if seed != None:
            self.seed = seed
        print(self.seed)
    
    def getRandom1(self,n):
        return int(time.time()) % n
    
    def getRandom2(self,n):
        obj = int()
        print(id(obj))
        return id(obj) %n
    
    def getRandom3(self, n):
        tmp =( (RandonGenerator.__A * self.seed)+RandonGenerator.__B) % RandonGenerator.__M
        self.seed = tmp
#        print(self.seed)
        return tmp % n
    
    


if __name__ == "__main__" :
    print("hello")
    rg = RandonGenerator()
    for i in range(20):
        time.sleep(2)
        print(rg.getRandom2(10))
            