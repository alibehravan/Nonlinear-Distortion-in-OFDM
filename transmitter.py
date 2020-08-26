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
import numpy as np
import math

    

class transmitter: 
    		# Initializer
    def __init__(self,sys):
        self.sys = sys            

    def modulator(self, SNR_per_bit):
        symbols = np.zeros((self.sys.Nc,1))
        if self.sys.modulation == 'BPSK':
            self.sys.BitsPerSymbol = 1
            Nbits = self.sys.BitsPerSymbol * self.sys.Nc       # Number of bits
            bits = np.random.binomial(n=1, p=0.5, size=Nbits)
            symbols = BitsToModSymbol(self.sys.BitsPerSymbol, bits)
            SNR = SNR_per_bit
        elif self.sys.modulation == 'QPSK':
            self.sys.BitsPerSymbol = 2
            Nbits = self.sys.BitsPerSymbol * self.sys.Nc
            bits = np.random.binomial(n=1, p=0.5, size=Nbits)
            symbols = BitsToModSymbol(self.sys.BitsPerSymbol, bits)
            SNR = SNR_per_bit+3
        elif self.sys.modulation == '16QAM':
            self.sys.BitsPerSymbol = 4
            Nbits = self.sys.BitsPerSymbol * self.sys.Nc
            bits = np.random.binomial(n=1, p=0.5, size=Nbits)
            symbols = BitsToModSymbol(self.sys.BitsPerSymbol, bits)
            SNR = SNR_per_bit+6
        elif self.sys.modulation == '64QAM':
            self.sys.BitsPerSymbol = 6
            Nbits = self.sys.BitsPerSymbol * self.sys.Nc
            bits = np.random.binomial(n=1, p=0.5, size=Nbits)
            symbols = BitsToModSymbol(self.sys.BitsPerSymbol, bits)
            SNR = SNR_per_bit+7.8
        return symbols, SNR, Nbits, bits

def BitsToModSymbol(BitsPerSymbol, Bits):    
    if BitsPerSymbol==1:
          Symbols = 1 - 2*Bits   
    BitVector = np.reshape(Bits, (len(Bits)//BitsPerSymbol , BitsPerSymbol))
    # The following contellations are all Gray mapped.  (Except for 32QAM.)
    if BitsPerSymbol == 2:
        Index = np.dot(BitVector , [2 , 1])
        Constellation = [ 1+1j , 1-1j , -1+1j , -1-1j ]/np.sqrt(2)
        Symbols = Constellation[Index]
    elif BitsPerSymbol == 4:
        Index = np.dot(BitVector , [8 , 4 , 2 , 1])
        Constellation = [
            1+1j  ,  1+3j ,  3+1j ,  3+3j ,
            1-1j  ,  1-3j ,  3-1j ,  3-3j ,
            -1+1j , -1+3j , -3+1j , -3+3j ,
            -1-1j , -1-3j , -3-1j , -3-3j]
        Constellation = np.divide(Constellation , math.sqrt( sum([(abs(k))**2 for k in Constellation]) / 16))
        Symbols = Constellation[Index]
    elif BitsPerSymbol == 6:
        Index = np.dot(BitVector , [32 , 16 , 8 , 4 , 2 , 1])
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
        Constellation = np.divide(Constellation , math.sqrt( sum([(abs(k))**2 for k in Constellation]) / 64))
        Symbols = Constellation[Index]
    return Symbols
