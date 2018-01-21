class IList( object ):
    """Some description that tells you it's abstract,
    often listing the methods you're expected to supply."""
    def get( self, index ):
        raise NotImplementedError( "Should have implemented this" )
    def display( self ):
        raise NotImplementedError( "Should have implemented this" )
    def size( self ):
        raise NotImplementedError( "Should have implemented this" )
    def add( self,e ):
        raise NotImplementedError( "Should have implemented this" )