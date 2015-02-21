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
print pd.isinteractive()

fig1, ax1 = plt.subplots(num=1,figsize=(6,1.0*img_ml.shape[0]/img_ml.shape[1]*6))
fig1.subplots_adjust(0,0,1,1);ax1.grid('off')
ax1.axis('off')
fig1.canvas.set_window_title(sys.argv[2])
im1 = ax1.imshow(img_ml)
fig1.canvas.draw()

fig2, ax2 = plt.subplots(3,1,num=2,figsize=[14,10])
ax2[0].hist(img_ml[:,:,0].reshape(img_ml.shape[0]*img_ml.shape[1]),bins=256,color='r')
ax2[0].set_xlim([0,256])
ax2[1].hist(img_ml[:,:,1].reshape(img_ml.shape[0]*img_ml.shape[1]),bins=256,color='g')
ax2[1].set_xlim([0,256])
ax2[2].hist(img_ml[:,:,2].reshape(img_ml.shape[0]*img_ml.shape[1]),bins=256,color='b')
ax2[2].set_xlim([0,256])
plt.show(block=False)

def f(x):
    return float(0.25) if x==True else float(1)
f = np.vectorize(f) 

while (1):
	x1,x2,x3=fig2.ginput(3)
	x1=int(round(x1[0]))
	x2=int(round(x2[0]))
	x3=int(round(x3[0]))
	img_darken=img_ml[:,:,0]*0

	img_darken=np.logical_and(np.logical_and(np.logical_or(img_ml[:,:,0]>x1+5,img_ml[:,:,0]<x1-5)\
		,np.logical_or(img_ml[:,:,1]>x2+5,img_ml[:,:,1]<x2-5)),\
				np.logical_or(img_ml[:,:,2]>x3+5,img_ml[:,:,2]<x3-5))
	img_darken=f(img_darken)
	img_darken=np.dstack((img_darken,img_darken,img_darken))
	img_darken=img_darken*img_ml
	fig1.clf()
	fig1, ax1 = plt.subplots(num=1,figsize=(6,1.0*img_darken.shape[0]/img_darken.shape[1]*6))
	fig1.subplots_adjust(0,0,1,1);ax1.grid('off')
	ax1.axis('off')
	fig1.canvas.set_window_title(sys.argv[2])
	im1 = ax1.imshow(img_darken.astype(np.uint8))
	fig1.canvas.draw()


	plt.show(block=False)
	fig2.clear()
	fig2,ax2 = plt.subplots(3,1,num=2)
	ax2[0].hist(img_ml[:,:,0].reshape(img_ml.shape[0]*img_ml.shape[1]),bins=256,color='r')
	ax2[0].set_xlim([0,256])
	ax2[0].axvspan((x1-5),(x1+5),facecolor='pink',alpha=0.25)
	ax2[1].hist(img_ml[:,:,1].reshape(img_ml.shape[0]*img_ml.shape[1]),bins=256,color='g')
	ax2[1].set_xlim([0,256])
	ax2[1].axvspan((x2-5),(x2+5),facecolor='pink',alpha=0.25)
	ax2[2].hist(img_ml[:,:,2].reshape(img_ml.shape[0]*img_ml.shape[1]),bins=256,color='b')
	ax2[2].set_xlim([0,256])
	ax2[2].axvspan((x3-5),(x3+5),facecolor='pink',alpha=0.25)
	plt.show(block=False)
