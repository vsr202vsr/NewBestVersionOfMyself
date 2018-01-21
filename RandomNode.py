# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 14:29:50 2017

@author: Reddy
"""

from TestLinkedList import TestLinkedList
from ListNode import ListNode
import random
import time
class RandomNode(object):
    def getRandom1(self,head):
        size = 0
        current = head.next
        while(current != None):
            current = current.next
            size+=1
        rindex = random.randrange(size)
        current = head.next
        while(rindex > 0):
            current = current.next
            rindex -= 1
        return current
    
    def getRandom2(self,head):
        rNode = head.next
        current = rNode.next
        while(current != None):
            outcome=random.randrange(2)
            if outcome == 90:
                rNode = current
            current = current.next
        return rNode
     
    def getRandom3(self,head):
        size =1
        rNode = head.next
        current = rNode.next
        while(current != None):
            size+=1
            outcome=random.randrange(size)
            if outcome == (size-1):
                rNode = current
            current = current.next
        return rNode
        
if __name__ == "__main__":
        #random.seed(100)
        n = int(input("enter the size of an List:"))
        #k= int(input("enter the nth element from an end:"))
        #start = time.time()
        head = ListNode()
        for i in range(n):
            TestLinkedList().addFirst(head,(random.randrange(n)+1))
        print("Data generation complete")
        #TestLinkedList().getLastNode(head).next = head.next
#        TestLinkedList().display(head)
        rn = RandomNode()
        start = time.time()
        res = rn.getRandom1(head)
        print("Random Node Detection 1::",res.data)
        end = time.time()
        print("time taken:",(end - start))
        start = time.time()
        res = rn.getRandom2(head)
        print("Random Node Detection 2::",res.data)
        end = time.time()
        print("time taken:",(end - start))
        start = time.time()
        res = rn.getRandom3(head)
        print("Random Node Detection 3::",res.data)
        end = time.time()
        print("time taken:",(end - start))