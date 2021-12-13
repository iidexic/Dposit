import json
import os

from pygame import image
from pygame import Surface




class spritelib:
    #MODES: Frame mode = 'frames', Slices mode = 'slices'
    def __init__(self, img_file = '',json_file = '', dir = 'assets',mode = 'frames'):
        self.img_file = image.load(os.path.join(dir,img_file))
        self.json_file = json_file
        self.mode = mode
        self.dir = dir
        if img_file != '' and json_file != '':
            self.load_sprites()
        elif img_file == '' and json_file == '':
            # attempt to load all images in directory
            pass
    def get_frames(self):
        self.spritedata = {}
        frames = self.json_file['frames']
        for f in frames:
            self.spritedata[f] = (frames[f])['frame']
        
    def get_slices(self):
        #! this should work but really gotta fucking check it
        self.spritedata = {}
        slices = (self.json_file['meta'])['slices']
        for s in slices:
            self.spritedata[s['name']] = ((s['keys'])[0])['bounds']
    
    def spritelist(self):
        self.sprites = {}
        for key,data in self.spritedata.items():
            data = list(data.values())          # maybe do this beforehand
            surf = Surface(data[2:4])
            surf.blit(self.img_file,(0,0),data)
            self.sprites[key] = surf
            
        
    def load_sprites(self):
        with open(os.path.join(self.dir,self.json_file)) as file:
            self.json_file = json.load(file)
        if self.mode == 'frames':
            self.get_frames()
        elif self.mode == 'slices':
            self.get_slices()
        self.spritelist()

#----------------------------
# Self-Testing:
#----------------------------
spritesheet = spritelib('SPRITESHEET.png','SPRITESHEET.json',mode = 'slices')

class levelsheet:
    def __init__(self, file,tileset, dir = 'assets'):
        with open(os.path.join(dir,file)) as f:
            self.json_file = json.load(f)
            self.info()
            self.make_levels()
            
    def info(self):
        self.gridsize = self.json_file['defaultGridSize']
        
        
    def get_layers(self):
        self.layers = (self.json_file['defs'])['layers']
    
    def make_levels(self):
        self.json_levels = self.json_data['levels']
        self.level_list = []
        for l in self.json_levels:
            self.level_list.append(level(l))
class level:
    def __init__(self,level_data,type = 'ldtk'):
        self.level_data = d = level_data
        if type == 'ldtk':
            self.ID = d['identifier']
            self.world_position = (d['worldx'],d['worldY'])
        