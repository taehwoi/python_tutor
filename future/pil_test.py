from PIL import Image, ImageFilter
import numpy as np

im = Image.open("homer.png")
im.show()
im = im.convert('RGB')
out = im.filter(ImageFilter.FIND_EDGES)
out.show("edges only")
out = im.transpose(Image.FLIP_LEFT_RIGHT)
out.show("homer in the mirror")
out = im.convert('LA')
out.show("noire homer")

# images are actually arrays!
pix = np.array(im)
print(pix)
