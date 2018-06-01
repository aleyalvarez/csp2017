import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw 

from PIL import ImageFont
'''Read image data'''
# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
pupper_file = os.path.join(directory, 'pupper.jpg')

# Open and show the pupper image in a new Figure window
pupper_img = PIL.Image.open(pupper_file)
fig, axes = plt.subplots(1, 1)


star_file = os.path.join(directory, 'star.png')
star_img = PIL.Image.open(star_file)

'''Modifications'''

# 1) paste image 'star' onto pupper
star_small = star_img.resize((70, 70)) #eye width and height measured in plt

pupper_img.paste(star_small, (400, 150)) 

# 2) remove all red from image
main_img = pupper_img
m = main_img.load()
 
# get x,y size 
s = main_img.size
 
# iterate through x and y (every pixel) 
for x in xrange(s[0]):
    for y in xrange(s[1]):
        r,g,b = m[x,y]
        # remove red from the pic 
        m[x,y] = 0,g,b

# 3) write text on image
font = ImageFont.truetype("arial.ttf", 100)

draw = PIL.ImageDraw.Draw(pupper_img, "RGBA")
draw.text((200, 1200), "A good boy!", fill=None, font=font)
'''Show image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(pupper_img, interpolation='none')
# Show the figure on the screen
fig.show()


fig.show()