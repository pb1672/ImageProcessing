import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
from scipy.ndimage.filters import median_filter as mf
import matplotlib.pylab as pd

path=os.path.join(sys.argv[1],sys.argv[2])
img_ml=nd.imread(path)

pd.ion()

ys = 6.5 * float(img_ml.shape[0])/float(img_ml.shape[1])

fig0, ax0 = plt.subplots(num=0,figsize=[6.5,ys])
ax0.axis('off')
fig0.subplots_adjust(0,0,1,1)
fig0.canvas.set_window_title(sys.argv[2])
img0 = ax0.imshow(img_ml)
fig0.canvas.draw()

fig2, ax2 = plt.subplots(3,1,num=2,figsize=[14,10])
ax2[0].hist(img_ml[:,:,0].reshape(img_ml.shape[0]*img_ml.shape[1]),bins=256,color='r')
ax2[0].set_xlim([0,256])
ax2[1].hist(img_ml[:,:,1].reshape(img_ml.shape[0]*img_ml.shape[1]),bins=256,color='g')
ax2[1].set_xlim([0,256])
ax2[2].hist(img_ml[:,:,2].reshape(img_ml.shape[0]*img_ml.shape[1]),bins=256,color='b')
ax2[2].set_xlim([0,256])
plt.show(block=False)

x_y=[[],[]]

while (1):
	for j in xrange(2):
		L = [int(round(i)) for i in fig0.ginput()[0]]
		x_y[j]=L

	x_y=zip(*x_y)
	img_crop=img_ml[min(x_y[0]):max(x_y[0]),min(x_y[1]):max(x_y[1]),:]
	if int(min(x_y[0]))==int(max(x_y[0])) and int(min(x_y[1]))==int(max(x_y[1])):
		fig2.clear()
		fig2, ax2 = plt.subplots(3,1,num=2,figsize=[10,10])
		ax2[0].hist(img_ml[:,:,0].reshape(img_ml.shape[0]*img_ml.shape[1]),bins=256,color='r')
		ax2[0].set_xlim([0,256])
		ax2[1].hist(img_ml[:,:,1].reshape(img_ml.shape[0]*img_ml.shape[1]),bins=256,color='g')
		ax2[1].set_xlim([0,256])
		ax2[2].hist(img_ml[:,:,2].reshape(img_ml.shape[0]*img_ml.shape[1]),bins=256,color='b')
		ax2[2].set_xlim([0,256])

		fig2.canvas.draw()
	else:

		fig2.clear()
		fig2, ax2 = plt.subplots(3,1,num=2,figsize=[10,8])
		ax2[0].hist(img_crop[:,:,0].reshape(img_crop.shape[0]*img_crop.shape[1]),bins=256,color='r')
		ax2[0].set_xlim([0,256])
		ax2[1].hist(img_crop[:,:,1].reshape(img_crop.shape[0]*img_crop.shape[1]),bins=256,color='g')
		ax2[1].set_xlim([0,256])
		ax2[2].hist(img_crop[:,:,2].reshape(img_crop.shape[0]*img_crop.shape[1]),bins=256,color='b')
		ax2[2].set_xlim([0,256])
		fig2.canvas.draw()
		 