import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
from scipy.ndimage.filters import median_filter as mf

img_ml = mf(1.0*(255-nd.imread(os.path.join('images','ml.jpg'))[::2,::2,::-1]),[8,2,1]).clip(0,255).astype(np.uint8)

ysize = 10.
xsize = ysize*float(img_ml.shape[1])/float(img_ml.shape[0])

fig0, ax0 = plt.subplots(num=0,figsize=[xsize,ysize])
fig0.subplots_adjust(0,0,1,1)
ax0.axis('off')
im0 = ax0.imshow(img_ml)
fig0.canvas.set_window_title('modified Mona Lisa')
fig0.canvas.draw()

plt.show()