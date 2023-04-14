# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 07:07:41 2021

@author: acer
"""
import numpy as np
import matplotlib.pyplot as plt
f=np.zeros([20,20])
f[10,10]=1
#f[15,15]=0.5
plt.imshow(f, cmap='gray')
g=np.zeros([3,3])
g[2,0]=1
g[1,1]=1
plt.imshow(g, cmap='gray')
g_r=g[::-1]
cov1=f*0;


plt.imshow(g_r, cmap='gray')
