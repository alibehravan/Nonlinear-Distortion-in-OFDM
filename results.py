#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:06:26 2020

@author: ealibeh
"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
import math
import random
import statistics as st

def plot_results(system,out,wanted_color):
    plt.figure(1)
    plt.plot(range(0,len(out.inst_PAPR_sym)), out.inst_PAPR_sym, color='r', label='before NL')
    plt.plot(range(0,len(out.inst_PAPR_sym_NL)), out.inst_PAPR_sym_NL, color=wanted_color, label='After NL')
    plt.grid(True)    
    plt.xlabel('Samples')
    plt.ylabel('Power')
    plt.legend(fontsize=18)
    plt.show()

    plt.figure(2)
    if system.modulation == 'BPSK':
        plt.plot(out.symbols_RX, '.', color=wanted_color)
        plt.plot(out.symbols_TX, 'o', color='r')
    else:   
        plt.plot(np.real(out.symbols_RX) , np.imag(out.symbols_RX), '.', color=wanted_color)
        plt.plot(np.real(out.symbols_TX) , np.imag(out.symbols_TX), 'o', color='r')
    plt.grid(True)
    plt.title('TX and RX symbols')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    plt.figure(3)
    plt.plot(system.SNR_per_bit, out.BER , color=wanted_color, label='without ML')
    plt.grid(True, which="both")
    plt.xlabel('SNR')
    plt.ylabel('BER')
    plt.legend(fontsize=18)
    plt.yscale("log")
    plt.show()


