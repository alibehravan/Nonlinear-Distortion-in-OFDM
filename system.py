#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 09:18:50 2020

@author: ealibeh

Parameters (Later make an object and move them to a separate parameter file)
"""
import numpy as np
import numpy as np
import math
    
class system: 
    		# Initializer
    def __init__(self):
        self.Nc = 600
        if self.Nc == 72:
            self.Nfft = 128
            self.BW = 1400000
        elif self.Nc == 180:
            self.Nfft = 256
            self.BW = 3000000
        elif self.Nc ==  300:
            self.Nfft = 512
            self.BW = 5000000
        elif self.Nc == 600:
            self.Nfft = 1024
            self.BW = 10000000
        elif self.Nc == 900:
            self.Nfft = 1536
            self.BW = 15000000
        elif self.Nc == 1200:
            self.Nfft = 2048                           
            self.BW = 20000000
        self.Nsym = 1000                              # Total number of OFDM sysmbols in the simulation
        self.modulation = '64QAM'                    # Choose from BPSK, QPSK,
        self.p_RB = 0.8                               # [watts] Assuming 40W over 50PRBs
        self.df = 15000                                  # Subcarrier spacing in Hz
        self.L = 4                                         # Oversampling ratio (in time) representing continuous signal
        self.K = 8                                      # Oversampling in frequency ( To see the waveforms and not only looking at the zero-crossing of OFDM we lookat the freq domain with higher resolution)
        self.T = 1/self.df                                    # Period of the baseband symbols (length of the pulse in time domain) in sec
        self.Ts = self.T/self.Nfft/self.L                                # Sampling period
        self.f0 = 30;                               # shift in frquency for the frequency domain plot
        self.SNR_per_bit = np.linspace(0,15,15)        # EB/N0

