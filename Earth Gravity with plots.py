# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:34:30 2022

@author: willi
"""

import numpy as np
import matplotlib.pyplot as plt

def gravitationalPull(x):   #en funktion som beregner g
    g_0 = 9.82
    R = 6.371e6
    
    g = np.zeros(np.size(x))    #en tom vektor g af samme størrelse som x bliver skabt
    
    g[x < R] = g_0 * x[x < R]/R     #g bliver beregnet for alle de tal i x som er mindre end R, og resultaterne bliver gemt i g vektoren
    
    g[x >= R] = g_0 * (R**2) / x[x >= R]**2 # g bliver beregnet for alle de tal i x som er større eller lig R, og resultaterne bliver gemt i g vektoren
    
    return g

x = np.arange(0, 1e7, 1e4)  #skaber vektor x, i intervallet 0 m til 10^7 m, med tal for hvert 10^4 m
plt.plot(x, gravitationalPull(x)) # plotter kurven
plt.show()  #viser kurven

