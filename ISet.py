# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 10:05:39 2017

@author: Reddy
"""

class ISet( object ):
    """Some description that tells you it's abstract,
    often listing the methods you're expected to supply."""
    def contains( self, key ):
        raise NotImplementedError( "Should have implemented this" )
    def display( self ):
        raise NotImplementedError( "Should have implemented this" )
    def size( self ):
        raise NotImplementedError( "Should have implemented this" )
    def remove( self,key ):
        raise NotImplementedError( "Should have implemented this" )
    def add( self,key):
        raise NotImplementedError( "Should have implemented this" )