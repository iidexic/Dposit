import json
import os

# LDTK: ALL IN ONE FILE (do not save levels to separate files)
# I could make it check and do it differently but I am lazy

class LDTK_parse:
    def __init__(self,file,dir = 'asset2',_islevel = False):
        self.path = os.path.join(dir,file)
        self.data = self.getjson()
        if _islevel == False:
            self.make_levels()
        elif _islevel == True:
            pass   
        
    def getjson(self):
        with open(self.path) as jfile:
            data = json.load(jfile)
        return data
    
    def make_levels(self):
        passlevel_list = self.data['']