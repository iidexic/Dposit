import json
import os


class spritelib:
    def __init__(self, img_file = '',json_file = '', dir = 'assets'):
        self.img_file = img_file
        self.json_file = json_file
        self.dir = dir
        
        if img_file != '' and json_file != '':
            self.load_sprites()
        elif img_file == '' and json_file == '':
            # attempt to load all images in directory
            pass
            
    def load_sprites(self):
        try:
            self.json_file = open(os.path.join(dir,self.json_file))
        except:
            print('failed to load sprite info from JSON')