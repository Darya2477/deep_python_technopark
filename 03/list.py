import copy
class CustomList(list):

    @staticmethod
    def equate_list_length(first: 'CustomList', second: 'CustomList'):
        first = copy.copy(first)
        second = copy.copy(second)
        max_len = max(len(first), len(second))

        while (len(first)<max_len):
            first.append(0)

        while (len(second)<max_len):
            second.append(0)
        
        return zip(first, second)
    
    def __init__(self, custom_list: 'CustomList' ):
        super().__init__(custom_list)

    @property
    def custom_list(self):
        """custom_list doc"""
        return self
    
    @custom_list.setter
    def custom_list(self, custom_list):
        self = custom_list

    @custom_list.deleter
    def custom_list(self):
        del self
        
    def __add__(self, other: 'CustomList'):
        return ([x+y for x, y in CustomList.equate_list_length(self, other)])  
      
    def __radd__(self, other:'CustomList'):
        if (isinstance(other, list)):
            return [x + y for x, y in zip(self, other)]

    def __sub__(self, other: 'CustomList'):
        return [x-y for x, y in CustomList.equate_list_length(self, other)]
    
    def __eq__(self, other: 'CustomList'):
        return True if sum(self)==sum(other) else False
    
    def __ne__(self, other:'CustomList'):
        return True if sum(self)!=sum(other) else False
    
    def __gt__(self, other: 'CustomList'):
        return True if (sum(self))>sum(other) else False
    
    def __ge__(self, other: 'CustomList'):
        return True if sum(self)>=sum(other) else False
    
    def __lt__(self, other:'CustomList'):
        return True if sum(self)<sum(other) else False
    
    def __le__(self, other:'CustomList'):
        return True if sum(self)<=sum(other) else False
        
    def __str__(self):
        return (self, (sum(self)))



        
