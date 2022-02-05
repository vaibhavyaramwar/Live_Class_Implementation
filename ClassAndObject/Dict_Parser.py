class dict_parser:
    
    def __init__(self,d):
        self.d = d
        
    def get_keys(self):
                
        try:    
            if type(self.d) == dict:
                return list(self.d.keys())
            else:
                raise Exception("Input is Not a Dictionary");
        except Exception as e:
            print(e)
            
    def get_values(self):
        
        try:
            if type(self.d) == dict:
                return list(self.d.values())
            else:
                raise Exception("Input is not a Dictionary")
        except Exception as e:
            print(e)
            
    def dict_check(self):
        
        try:
            if type(self.d) != dict:
                raise Exception("Input is not a Dictionary")
            else:
                print("Input is Dictionary")
        except Exception as e:
            print(e)       
      
    def dict_user_input(self,newDict):
        
        try:
            if type(newDict) == dict:
                
                print(newDict.items())
                
            else:
                raise Exception("Input is not a Dictionary")
        except Exception as e:
            print(e)
            
    
    def dict_add_key_vale(self,key,value):
        
        self.d[key] = value
        return self.d
        