#!/usr/bin/env python3

# Packages
import os
# Import Python Image Library
from PIL import Image

gallerypath = 'images/gallery/'

# Wrapper for image
def imwrap(path):

    return '<div class="col-4"><span class="image fit"><img src="images/gallery/' + path + ' alt="" /></span></div>'

def openim(path):

    if 

for impath in os.listdir(gallerypath):
    if 'Gallery' not in impath:
        print(gallerypath+impath)
        x = Image.open(gallerypath+impath)
        x.show()

# Open press
file = open('press.html','r')
html = file.read().split('<!-- Gallery -->') # Read and split file
