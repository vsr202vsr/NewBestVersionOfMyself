# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 14:56:45 2017

@author: Reddy
"""

from TestLinkedList import TestLinkedList
from ListNode import ListNode
import random
import time
class FindKthfromEnd(object):
    def findKthElementfromEnd1(self,head,k):
        size = 0
        #self.current = ListNode()
        current = head.next
        while(current != None):
            current = current.next
            size+=1
        i = 1
        current = head.next
        while(i <= (size-k)):
            i+=1
            current = current.next
        return current
    def findKthElementfromEnd2(self, head,k):
        first,second = head,head
        for i in range(k):
            second = second.next
        while(second != None):
            first = first.next
            second = second.next
        return first
    def findKthElementfromEnd3(self, head,k):
        first,second,third = head,head,head
        #for i in range(k):
        # second = second.next
        while(second != None):
            third = first
            first = second
            for i in range(k):
                if(second != None):
                    second = second.next
        first = third
        second = third
        for i in range(k):
            second = second.next
        while(second != None):
            first = first.next
            second = second.next
        return first

    
if __name__ == "__main__":
        random.seed(100)
        n = int(input("enter the size of an List:"))
        k= int(input("enter the nth element from an end:"))
        start = time.time()
        head = ListNode()
        for i in range(n):
            TestLinkedList().addFirst(head,(random.randrange(n)+1))
        print("Data generation complete")
        TestLinkedList().display(head)
        res = FindKthfromEnd().findKthElementfromEnd3(head,k)
        print("kth element::",res.data)
        end = time.time()
        print("time taken:",(end - start))