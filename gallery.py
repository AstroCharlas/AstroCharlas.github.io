#!/usr/bin/env python3

# Packages
import os
import sys
from PIL import Image

# Path to gallery
gallerypath = 'images/gallery/'

# HTML file
htmlsection = '<!-- Gallery -->\n'

# Remove pesky mac files
if os.path.exists(gallerypath + '.DS_Store'): os.remove(gallerypath + '.DS_Store')

# Iterate over images in gallery that are not final products
for i,impath in enumerate([x for x in os.listdir(gallerypath) if (not 'Gallery' in x)]):

    # Load Photo
    try:
        img = Image.open(gallerypath+impath)
    except: 
        print('Unable to load',gallerypath+impath,'.')
        print('Please ensure that this is an image file.')
        print('Note, not all image formats are supported.')
        print('If this is an image, please convert to JPG or PNG.')
        sys.exit(1)
    
    # Crop photo
    size = min(img.size)
    width, height = img.size
    img = img.crop(((width-size)/2,(height-size)/2,(width+size)/2,(height+size)/2))

    # Save photo
    imname = gallerypath+'Gallery'+str(i)+'.jpeg'
    img.save(imname,format='JPEG')

    # HTML addition
    htmlsection += '\t'*11 + '<div class="col-4"><span class="image fit"><img src="' + imname + '" alt="" /></span></div>\n'

# Open and edit press html
file = open('press.html','r+')
html = file.read().split('<!-- Gallery -->') # Read and split file

# Add our section and close it with the tag
html[1] = htmlsection+'\t'*11+'<!-- Gallery -->'

# Find beggining of file and write
file.seek(0)
file.write(''.join(html))
file.truncate() # Throw away the rests
file.close()