# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 13:41:00 2019

@author: abhis
"""

import numpy as np
import matplotlib.pyplot as plt


def Last_Seen(VanEck):
    index = np.argwhere(np.array(VanEck)==VanEck[-1]).T[0]
    if len(index)==1:
        return 0
    else:    
        return index[-1]-index[-2]
    
    

N = 10**5
VanEck = [0,0]
for i in range(N-2):
    VanEck.append(Last_Seen(VanEck))

#f=lambda n,l=0,*s:f(n-1,l in s and~s.index(l),l,*s)if n else-l
#for i in range(N):
#	VanEck.append(f(i))

plt.close('all') 
plt.figure()
plt.plot(np.arange(N),VanEck,'o')

plt.figure()
plt.hist(VanEck)
