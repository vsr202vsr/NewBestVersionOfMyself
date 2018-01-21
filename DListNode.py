# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 13:22:24 2017

@author: Reddy
"""
class DListNode(object):
    def __init__(self,key = None, value=None):
        if key != None and value != None:
            self.key = key
            self.value = value
        self.prev= self.next= self
