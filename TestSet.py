# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:59:53 2017

@author: Reddy
"""
#import java.util.Random;
#import java.util.UUID;
import random
import uuid

class TestSet(object):
    def testSet(self,cache, n):
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
    #TestSet().testset(testSet(10), n)