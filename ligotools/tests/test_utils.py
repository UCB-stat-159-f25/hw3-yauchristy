from scipy.io import wavfile
from scipy.interpolate import interp1d
from ligotools.utils import whiten, write_wavfile, reqshift
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import pytest

def test_whiten():
    fs = 1000
    NFFT = 4*fs
    strain = [1,2,3,4]
    Pxx_H1, freqs = mlab.psd(strain, Fs = fs, NFFT = NFFT)
    psd_H1 = interp1d(freqs, Pxx_H1)
    strain_whitened = whiten(strain,psd_H1,0.01)
    assert len(strain_whitened) == len(strain)

def test_reqshift():
    strain = [1,2,3,4]
    fs = 4096
    fshift = 400.
    speedup = 1.
    fss = int(float(fs)*float(speedup))
    strain_shifted = reqshift(strain,fshift=fshift,sample_rate=fs)
    assert len(strain_shifted) == len(strain)