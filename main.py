# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 13:41:00 2019

@author: abhis
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.rc('text', usetex=True)
plt.rc('font',\
       **{'family':'sans-serif','sans-serif':['Helvetica']})
#       **{'family':'serif','serif':['Times']})

plt.rc('font',size=12)

def Last_Seen(VanEck):
    index = np.argwhere(np.array(VanEck)==VanEck[-1]).T[0]
    if len(index)==1:
        return 0
    else:    
        return index[-1]-index[-2]
    
    
#%% Initialization
N = 10**5
VanEck = np.ones((N,))
VanEck[0] = 0
VanEck[1]=0
#%%
for i in range(2,N-1):
    VanEck[i+1]=Last_Seen(VanEck[:i])
    

#f=lambda n,l=0,*s:f(n-1,l in s and~s.index(l),l,*s)if n else-l
#for i in range(N):
#	VanEck.append(f(i))
#%% Plotting
plt.close('all') 

idxplot = 10**5
SeqIdx = np.arange(N)
plt.figure()
plt.plot(SeqIdx[:idxplot],VanEck[:idxplot],'.')
plt.axis('square')
plt.xlabel('Index')
plt.ylabel('Number')
plt.tight_layout()

#plt.figure()
#plt.loglog(np.arange(N),VanEck,'.')
#plt.axis('square')
#plt.xlabel('Index')
#plt.ylabel('Number')
#plt.yscale('log', nonposy='clip')
#plt.xscale('log')
#plt.tight_layout()


plt.figure()
plt.subplot(211)
plt.hist(VanEck[:idxplot],bins=50)
plt.xlabel('Number')
plt.ylabel('Counts')
plt.tight_layout()

plt.subplot(212)
plt.hist(VanEck[:idxplot],bins = 'auto')
plt.yscale('log', nonposy='clip')
plt.xscale('log')
plt.xlabel('Number')
plt.ylabel('Counts')
plt.tight_layout()