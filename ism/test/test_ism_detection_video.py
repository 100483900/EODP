import logging

from common.io.writeToa import readToa
import numpy as np
from config.globalConfig import globalConfig
import os
import matplotlib.pyplot as plt


# Inits
globalConfig = globalConfig()
auxdir = 'auxiliary'
indir = "EODP_TER/EODP-TS-ISM/input"
outdir = "EODP_TER/EODP-TS-ISM/output"
outrefdir = "EODP_TER/EODP-TS-ISM/output_ref"

# PASS/FAIL Criteria 1 TOA
for band in globalConfig.bands:
    try:
        toa = readToa(outdir, globalConfig.ism_toa + band + '.nc')
        toa_ref = readToa(outrefdir, globalConfig.ism_toa + band + '.nc')
        error = np.divide(np.abs(toa-toa_ref), toa, out=np.zeros_like(toa), where=toa != 0)*100 # Div handling div/0
        assert (error < 0.01).sum() > toa_ref.size*0.997
        print(f'PASSED for {band}')
    except AssertionError as e:
        print(f'TEST failed for band: {band}. Points exceeding 0.01 deviation: {(error > 0.01).sum()} of {toa_ref.size-toa_ref.size*0.997} allowed')

# PASS/FAIL Criteria 4 Saturated Pixel
for band in globalConfig.bands:
    toa = readToa(outdir, globalConfig.ism_toa + band + '.nc')
    bit_depth = 12
    saturated_pixels = toa[toa >= 2 ** bit_depth - 1].sum()
    percen_saturated_pixels = saturated_pixels/toa.sum()*100
    print(f'TEST Saturated pixels for {band}: {saturated_pixels} - {round(percen_saturated_pixels,2)}%')

