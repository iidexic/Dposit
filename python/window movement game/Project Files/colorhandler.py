from pygame import image
import os

class colorpalette:
    def __init__(self,palettefile):
        self.file = palettefile
        palimg = image.load(os.path.join('assets',palettefile))
        self.palette = palimg.get_palette()

    #def make_dict(self): # if want to build dictionary of color descriptors. seems pointless tho
    
test = colorpalette('japanese-woodblock-32x.png')
print(test.palette)
