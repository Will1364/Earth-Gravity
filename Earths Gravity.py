# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:12:24 2022

@author: william
"""

import math
import numpy as np



def gravitationalPull(x):
    g_0 = 9.82
    R = 6.371e6
    
    if R <= x:                  # hvis x er over jordens overflade beregnes g på en måde
        g = g_0 * (R**2)/(x**2)
    if x >= 0 and x < R:        # hvis x er under jordens overflade berenes g på en anden måde
        g = g_0 * x / R
    
    return g

