#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 09:18:50 2020

@author: ealibeh
"""

"""
Parameters (Later make an object and move them to a separate parameter file)
"""
import numpy as np
import math

    

class receiver: 
    		# Initializer
    def __init__(self,sys):
        self.sys = sys            


    def demodulator(self, symbols):
        if self.sys.modulation ==  'BPSK':
            bits = 0.5*(1-np.sign(np.real(symbols)));
        elif self.sys.modulation == 'QPSK':
            softbits =  [np.real(symbols) , np.imag(symbols)]
            bits = (1 - np.reshape(np.sign(softbits), len(symbols)*2, order = 'F')) // 2
        elif self.sys.modulation == '16QAM':
            Constellation = [
            1+1j  ,  1+3j ,  3+1j ,  3+3j ,
            1-1j  ,  1-3j ,  3-1j ,  3-3j ,
            -1+1j , -1+3j , -3+1j , -3+3j ,
            -1-1j , -1-3j , -3-1j , -3-3j]
            symbols = symbols * math.sqrt( sum([(abs(k))**2 for k in Constellation]) / 16)
            bits = []
            for i in range (0,len(symbols)):
                distance = abs(symbols[i]-Constellation)
                index = np.argmin(distance, axis=0)
                sym_to_bits = [int(x) for x in format(index, '#06b')[2:]]
                bits.extend(sym_to_bits) 
        elif self.sys.modulation == '64QAM':
            Constellation = [
                3+3j ,  3+1j ,  1+3j ,  1+1j ,  3+5j ,  3+7j ,  1+5j ,  1+7j ,
                5+3j ,  5+1j ,  7+3j ,  7+1j ,  5+5j ,  5+7j ,  7+5j ,  7+7j ,
                3-3j ,  3-1j ,  1-3j ,  1-1j ,  3-5j ,  3-7j ,  1-5j ,  1-7j ,
                5-3j ,  5-1j ,  7-3j ,  7-1j ,  5-5j ,  5-7j ,  7-5j ,  7-7j ,
                -3+3j , -3+1j , -1+3j , -1+1j , -3+5j , -3+7j , -1+5j , -1+7j ,
                -5+3j , -5+1j , -7+3j , -7+1j , -5+5j , -5+7j , -7+5j , -7+7j ,
                -3-3j , -3-1j , -1-3j , -1-1j , -3-5j , -3-7j , -1-5j , -1-7j ,
                -5-3j , -5-1j , -7-3j , -7-1j , -5-5j , -5-7j , -7-5j , -7-7j 
                ]
            symbols = symbols * math.sqrt( sum([(abs(k))**2 for k in Constellation]) / 64)
            bits = []
            for i in range (0,len(symbols)):
                distance = abs(symbols[i]-Constellation)
                index = np.argmin(distance, axis=0)
                sym_to_bits = [int(x) for x in format(index, '#08b')[2:]]
                bits.extend(sym_to_bits) 

        return bits
