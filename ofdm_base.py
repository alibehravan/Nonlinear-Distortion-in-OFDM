"""
Code originally copied from my MATLAB/ofdm_base directory which is a simple baseband  OFDM with NL
Importing Libraries
"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
import tensorflow as tf 
import math
import random
import statistics as st

from system import system
from output import output
from transmitter import transmitter
from receiver import receiver
from nonlinearity import soft_limiter  
from results import plot_results

sys = system()
tx = transmitter(sys)
rx = receiver(sys)  
out = output()

def main():
    PAPR_sym = zeros(sys.Nsym);
    inst_PAPR = np.zeros((sys.Nsym,sys.Nfft*sys.L))
    inst_PAPR_NL = np.zeros((sys.Nsym,sys.Nfft*sys.L))
    real_snr_per_info_bit = zeros(len(sys.SNR_per_bit))
    accumulate_RX_symbols = [];
    PAPR = []
    real_snr = zeros(len(sys.SNR_per_bit))
    out.BER = zeros(len(sys.SNR_per_bit))
    for snr_idx in range(0, len(sys.SNR_per_bit)):
        error = 0
        for sym_idx in range(0, sys.Nsym):
            symbols, SNR, Nbits, bits = tx.modulator(sys.SNR_per_bit[snr_idx])
            symbols_zero_padded = np.concatenate((symbols[0:sys.Nc//2], np.zeros((sys.Nfft-sys.Nc)), symbols[-sys.Nc//2:]))
            symbols_oversampled = np.concatenate((symbols_zero_padded[0:sys.Nfft//2] , 
                                                 np.zeros((sys.L-1)*sys.Nfft) , symbols_zero_padded[-sys.Nfft//2:]))
            OFDM_sym = sqrt(sys.L*sys.Nfft) * np.fft.ifft(symbols_oversampled, sys.L*sys.Nfft)
            #OFDM_sym = sqrt(sys.Nfft) * np.fft.ifft(symbols_oversampled, sys.L*sys.Nfft)
            out.inst_PAPR_sym = abs(OFDM_sym)**2 / mean(abs(OFDM_sym)**2)
            inst_PAPR[sym_idx,:] = np.array(out.inst_PAPR_sym) 
            PAPR_sym[sym_idx] = np.amax(out.inst_PAPR_sym)
            
            TX_signal = OFDM_sym
            #TX_signal = soft_limiter(OFDM_sym)
            
            out.inst_PAPR_sym_NL = abs(TX_signal)**2 / mean(abs(TX_signal)**2)
            inst_PAPR_NL[sym_idx,:] = np.array(out.inst_PAPR_sym_NL) 

            # Channel            
            P_n = 1/power(10,(SNR/10))
            
            #P_n = sqrt(mean(abs(TX_signal)**2))/power(10,(SNR/10))
            noise = sqrt(P_n) * (np.random.normal(size = len(TX_signal)) + 1j*np.random.normal(size = len(TX_signal))) / sqrt(2)
            RX_signal = TX_signal + noise;
            #Average SNR on each OFDM symbol. If OFDM symbols in different modulation carry the same number of bits, then they are comparble
            real_snr_per_info_bit[snr_idx] = (sum(abs(TX_signal)**2)/Nbits) / mean(abs(noise)**2)
            
            OFDM_sym_R = RX_signal
            symbols_oversampled_RX = 1/(sqrt(sys.L*sys.Nfft))*np.fft.fft(OFDM_sym_R,sys.L*sys.Nfft);
            #symbols_oversampled_RX = 1/(sqrt(sys.Nfft))*np.fft.fft(OFDM_sym_R,sys.L*sys.Nfft);
            symbols_zero_padded_RX = np.concatenate((symbols_oversampled_RX[0:sys.Nfft//2] , symbols_oversampled_RX[-sys.Nfft//2:]))
            out.symbols_RX = np.concatenate((symbols_zero_padded_RX[0:sys.Nc//2] , symbols_zero_padded_RX[-sys.Nc//2:]))
            out.symbols_TX = symbols
            bits_RX = rx.demodulator(out.symbols_RX)
            error = error + sum(abs(bits - bits_RX))
        real_snr[snr_idx] = mean(real_snr_per_info_bit)
        out.BER[snr_idx] = error/(sys.Nsym*Nbits)
        PAPR.append(PAPR_sym)
            
            
    plot_results(sys,out,'b')
    
if __name__ == "__main__":
    main()