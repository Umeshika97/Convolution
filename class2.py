# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 09:17:04 2021

@author: hiran
"""
import numpy as np
import matplotlib.pyplot as plt

def image(data,grid_size=5,grid="on",cmap='gray'):
    d=data
    plt.figure()
    plt.imshow(d,cmap='gray',extent=[0,d.shape[0],d.shape[1],0])
    if grid=="on":
        plt.pcolormesh(d, edgecolors='midnightblue', linestyle='dotted',linewidth=1,cmap='gray')
    ax = plt.gca()
    ax.set_xticks(np.arange(0.5, d.shape[0], grid_size))
    ax.set_xticklabels((np.arange(0.5, d.shape[0], grid_size)-0.5).astype(int))
    ax.set_yticks(np.arange(0.5, d.shape[1], grid_size))
    ax.set_yticklabels((np.arange(0.5, d.shape[1], grid_size)-0.5).astype(int))
    plt.show()
    
    
f=np.zeros([20,20])
f[10,10]=1
f[15,15]=0.5

image(f)
plt.imshow(f,cmap='gray')

g=np.array([[0,0,1],[0,1,0],[0,0,0]])
g[2,0]=1
g[1,1]=1

# plt.imshow(g,cmap='gray')

# g_r

# cov1=