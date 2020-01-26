from collections import MutableMapping
class MapBase(MutableMapping):
    '''This is a Abstract Base class that includes non public class _item.
    This class will provide methods of MutableMapping which are already implemented 
    and some methods which will be declared in classes extensdiing these base classes '''
    class _item:
        def __init__(self,k, v):
            self._key=k
            self._value=v

        def __eq__(self, other):
            return self._key==other._key

        def __nq__(self, other):
            return (self==other)

        def __lt__(self, other):
            return self._key < other._key
