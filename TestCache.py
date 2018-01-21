# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 14:31:14 2017

@author: Reddy
"""
#import java.util.Random;
#import java.util.UUID;
import random
import uuid
from LinkedHashMapCache import LinkedHashMapCache

class TestCache(object):
    def testCache(self,cache, n):
        tmp = None
        for i in range(n):
            key = uuid.uuid4()#UUID.randomUUID().toString()
            value = random.randrange(1000)
            cache.add(key, value)
            if(i == 3):
                tmp = key
#            cache.display()
        print(cache.get(tmp))
        cache.display()
        
if __name__ == "__main__" :
    n = int(input("enter the size"))
    TestCache().testCache(LinkedHashMapCache(10), n)