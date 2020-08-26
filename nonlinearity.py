#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:00:27 2020

@author: ealibeh
"""
import numpy as np
import math
import random
import statistics as st


def soft_limiter(x):
    sqrt_power_x = np.sqrt(st.mean(abs(x)**2))
    IBO = 3
    limit = sqrt_power_x  * np.sqrt(10**(IBO/10))
    #limit = 0.7  # use 1 for some clipping or 0.5 for more clipping,..
    #x = x/sqrt_power_x
    y = x
    y[np.where(abs(x) > limit)] = limit * np.exp(1j * np.angle(x[np.where(abs(x) > limit)]))
    y = y * sqrt_power_x/np.sqrt(st.mean(abs(y)**2))
    return y

