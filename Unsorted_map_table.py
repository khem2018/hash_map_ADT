class Unsorted_table_map(MapBase):
    
    def __init__(self):
        self._table = []
        
    def __iter__(self):
        for item in self._table:
            yield item._key
                       
    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise Exception('KeyError: Key not found')
        
    def __setitem__(self, k, v):
        for item in self._table:
            if k ==item._key:
                item._value=v
                return
        self._table.append(self._item(k,v))
        
    def __delitem__(self,k):
        for item in range(len(self._table)):
            if k == item._key:
                self._table.pop(item)    
                return
        raise Exception('KeyError: Key not found')
                
    def __len__(self):
        return len(self._table)
