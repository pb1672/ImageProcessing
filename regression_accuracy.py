import os
import sys
import time
import scipy.ndimage as nd
import matplotlib.pyplot as plt
import operator
import math
import numpy as np


img = nd.imread('images/digits.png')
xs = 10.
ys = xs*float(img.shape[0])/float(img.shape[1])
fIndex = {}
reject = []

xs=xs/1.5
fig12, ax12 = plt.subplots(num=1,figsize=[xs,xs])
fig12.subplots_adjust(0,0,1,1)
ax12.axis('off')
numbers = img.reshape(50,20,100,20).transpose(0,2,1,3).reshape(5000,20,20)

im12 = ax12.imshow(numbers[0])
fig12.canvas.draw()

fig12.show()

avg_numbers = np.array([numbers[k*500:(k+1)*500].mean(0) for k in range(0,10)])


for a in range(10):

    wrong = 0
    error = {}

    l = []

    for i in xrange(500):
        #index = a * 500 + i


        inverse = np.linalg.inv(np.dot(avg_numbers.reshape(10,400),avg_numbers.reshape(10,400).transpose()))
        yy = np.dot(avg_numbers.reshape(10,400),numbers[a * 500 + i].flatten())

        l.append(np.dot(inverse,yy))

        if np.argmax(np.dot(inverse,yy)) != a:
            fIndex[a * 500 + i] = np.argmax(np.dot(inverse,yy))
            reject.append(a * 500 + i)
            wrong += 1
            if np.argmax(np.dot(inverse,yy)) not in error:
                error[np.argmax(np.dot(inverse,yy))] = 1
            else:
                error[np.argmax(np.dot(inverse,yy))] += 1 
        else:
            pass

    xs = 6
    ys = 8
    fig0, ax0 = plt.subplots(10,1,figsize=[xs,ys], sharex=True)

    sorted_error = sorted(error.items(), key=operator.itemgetter(1), reverse = True)
    v = np.vstack(l)
    add = v.T


    for j in range(0,10):
        ax0[j].hist(add[j], bins = 100, color='green')
        [i.set_yticklabels('') for i in ax0]
        ax0[j].set_title("Known %s's Against %s's"% (a,str(j)), fontsize=12)

    fig0.subplots_adjust(hspace=2)
    fig0.subplots_adjust(.1,.1,.95,.95)
    fig0.canvas.draw()

    fig0.show()

    print "%s%% of %s's were incorrectly identified, the most common guess for those failures was %s's" % \
    ((wrong/500.0) * 100, a, sorted_error[0][0])

t = 0.0
while t<30.:
    i = int(math.floor(len(reject)*np.random.rand()))
    a = reject[i]

    if t == 0.0:
        im12.set_data(numbers[a])
        lab = ax12.text(0,0, 'Guess:  ', va = 'top', fontsize = 22, color = 'b')
        lab.set_text('Guess: {0}'.format(fIndex[a]))
    else:
        lab.remove()
        im12.set_data(numbers[a])
        lab = ax12.text(0,0, 'Guess:  ', va = 'top', fontsize = 22, color = 'b')
        lab.set_text('Guess: {0}'.format(fIndex[a]))

    fig12.canvas.draw()
    fig12.show()
    time.sleep(1.0)
    t = time.time()-time.time()

plt.clf('all')
fIndex = {}
reject = []

print "\n"
print "Removing zero point offset:\n"

for a in range(10):

    wrong = 0
    error = {}

    l = []

    for i in xrange(500):

        P  = np.vstack((avg_numbers.reshape(10,400), np.ones(400))).transpose()
        inverse = np.linalg.inv(np.dot(np.vstack((avg_numbers.reshape(10,400), np.ones(400))),P))
        yy = np.dot(np.vstack((avg_numbers.reshape(10,400), np.ones(400))),numbers[a * 500 + i].flatten())

        vect = np.dot(inverse,yy)[0:10]
        l.append(vect[0:10])

        if np.argmax(vect) != a:
            fIndex[a * 500 + i] = np.argmax(vect)
            reject.append(a * 500 + i)
            wrong += 1
            if np.argmax(vect) not in error:
                error[np.argmax(vect)] = 1
            else:
                error[np.argmax(vect)] += 1 
        else:
            pass

    xs = 10
    ys = 8
    fig1, ax1 = plt.subplots(10,1,figsize=[xs,ys], sharex=True)

    sorted_error = sorted(error.items(), key=operator.itemgetter(1), reverse = True)
    v = np.vstack(l)
    add = v.T

    for j in range(0,10):
        ax1[j].hist(add[j], bins = 100, color='green')
        [i.set_yticklabels('') for i in ax1]
        ax1[j].set_title("Known %s's Against %s's"% (a,str(j)), fontsize=10)

    fig1.subplots_adjust(hspace=2)
    fig1.subplots_adjust(.1,.1,.9,.9)
    fig1.canvas.draw()

    print "%s%% of %s's were incorrectly identified, the most common guess for those failures was %s's" % \
    ((wrong/500.0) * 100, a, sorted_error[0][0])

plt.show()