# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 12:46:59 2017

@author: Reddy
"""
import random
import numpy as np
import time

"""
Big O of <= m*n or n*n 
"""
def findCommonElements1(in1,in2):
    count = 0;
#    print(np.size(in1),np.size(in2))
    for i in range(in1.size):
        for j in range(in2.size):
            if (in1[i] == in2[j]):
                count+=1
    return count

def findCommonElements2(in1,in2):
    count = 0
    in1=np.sort(in1)
    in2=np.sort(in2)
    i = 0
    j = 0
#    print(in1,in2)
    while(i < np.size(in1) and j < np.size(in2)):
        if (in1[i] < in2[j]):
            i+=1
        elif (in1[i] > in2[j]):
            j+=1
        else:
            i+=1
            j+=1
            count+=1
    return count
	
def findCommonElements3(in1,in2):
    count = 0
#    in1=np.sort(in1)
    for i in in2:
#        print(in1)
        if np.searchsorted(in1, i):
            count+=1
    return count

def removeDuplicates(in1):
    hset = set() 
    for i in in1:
        hset.add(i)
    l=[]
    for j in hset:
        l.append(j)
    return np.array(l)
        
            
		

if __name__ == "__main__" :
    n= int(input("enter the size of arrays"))
    in1=[]
    in2 =[]
    random.seed(100)
    for i in range(n):
        in1.append(random.randrange(i+1))
        in2.append(random.randrange(i+1))    
    
#==============================================================================
#     in3= removeDuplicates(in1)
#     in4= removeDuplicates(in2)
#==============================================================================
    in3= np.array(in1)
    in4= np.array(in2)
#    print(in3,in4)
    start = time.time()
    count = findCommonElements2(in3, in4)
    print(count);
    end = time.time()
    print(end - start)
  
