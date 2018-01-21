# -*- coding: utf-8 -*-
import random
import time
from IList import IList
from ArrayList import ArrayList
from LinkedList import LinkedList

class TestList(object):
    def testlist(self,lst,n):
        random.seed(100)
        for i in range(n):
            lst.add(random.randrange(n))
        #lst.display()
                    
if __name__ == "__main__" :
    n= int(input("enter the size of arrays"))
    tl= TestList()
    start = time.time()
    #d= ArrayList()
    d = LinkedList()
    tl.testlist(d, n)
    end = time.time()
    print(end - start)
           

