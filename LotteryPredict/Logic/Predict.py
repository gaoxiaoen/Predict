# -*- coding: utf-8 -*-
#使用神经网络算法的监督学习算法进行预测

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def nonline(x,deriv=False):
	# print "nonline x="
	# print x
	# raw_input("继续")
	if (deriv==True):
		return x*(1-x)
	return 1/(1+np.exp(-x))

X = np.array([  [0,0,1],
				[0,1,1],
				[1,0,1],
				[1,1,1] ])
y = np.array([[0,0,1,1]]).T 

np.random.seed(1)

syn0 = 2*np.random.random((3,1)) -1
print "before .."
print np.random.random((3,1))
print "end .."

print "syn0 is :"
print syn0
print "is end"

for iter in xrange(1000):
	l0 = X
	l1=nonline(np.dot(l0,syn0))

	l1_error = y - l1

	l1_delta = l1_error * nonline(l1,True)
	syn0 += np.dot(l0.T,l1_delta)


print "Output After Training:"
print l1



def update_line(num,data,line):
	line.set_data(data[...,:num])
	return line

fig1 = plt.figure()

data = np.random.rand(2,25)
l,=plt.plot([],[],'r-')
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel('x')
plt.title('test')
line_ani = animation.FuncAnimation(fig1,update_line,25,
	fargs=(data,1),interval=50,blit=True)


plt.show()



