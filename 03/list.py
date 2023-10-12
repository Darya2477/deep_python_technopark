class CustomList(list):
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
        max_len = max(len(self), len(other))

        l1 = self
        l2 = other
        res=[]

        while (len(l1)<max_len):
            l1.append(0)

        while (len(l2)<max_len):
            l2.append(0)
        
        for i in range(max_len):
            res.append(l1[i]+l2[i])
            
        return res



        
