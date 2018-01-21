# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 23:07:39 2017

@author: Reddy
"""

from TestLinkedList import TestLinkedList
from ListNode import ListNode
import random
import time
class LoopDetection(object):
    def hasLoop1(self,head):
        hset = set()
        current = head.next
        while(current != None):
            if (current in hset):
                return True
            else:
                hset.add(current)
            current = current.next
        return False 
    
    def hasLoop2(self,head):
        slow=fast= head
        slow = slow.next
        if(fast.next != None):
            fast = fast.next.next
        while(True):
            #print("interate")
            if (slow != fast):
                slow = slow.next
                if(fast!= None and fast.next != None):
                    fast = fast.next.next
                else:
                    return False
            else:
                return True
    #Syntax change nothing new in loop3       
    def hasLoop3(self,head):
        slow=fast= head
        while(fast!= None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            #print("interate") 
            if (slow == fast):
                return True
        return False
        
if __name__ == "__main__":
        random.seed(100)
        n = int(input("enter the size of an List:"))
        #k= int(input("enter the nth element from an end:"))
        #start = time.time()
        head = ListNode()
        for i in range(n):
            TestLinkedList().addFirst(head,(random.randrange(n)+1))
        print("Data generation complete")
        #TestLinkedList().getLastNode(head).next = head.next
        #TestLinkedList().display(head)
        LD = LoopDetection()
        start = time.time()
        res = LD.hasLoop1(head)
        print("Loop Detection 1::",res)
        end = time.time()
        print("time taken:",(end - start))
        start = time.time()
        res = LD.hasLoop2(head)
        print("Loop Detection 2::",res)
        end = time.time()
        print("time taken:",(end - start))
        start = time.time()
        res = LD.hasLoop3(head)
        print("Loop Detection 3::",res)
        end = time.time()
        print("time taken:",(end - start))