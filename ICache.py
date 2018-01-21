# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 13:15:00 2017

@author: Reddy
"""

class ICache( object ):
    """Some description that tells you it's abstract,
    often listing the methods you're expected to supply."""
    def get( self, key ):
        raise NotImplementedError( "Should have implemented this" )
    def display( self ):
        raise NotImplementedError( "Should have implemented this" )
    def size( self ):
        raise NotImplementedError( "Should have implemented this" )
    def capacity( self ):
        raise NotImplementedError( "Should have implemented this" )
    def add( self,key, value):
        raise NotImplementedError( "Should have implemented this" )