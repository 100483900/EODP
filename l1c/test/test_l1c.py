import logging
from common.io.writeToa import readToa
import numpy as np
from config.globalConfig import globalConfig
import os
import matplotlib.pyplot as plt

# Inits
globalConfig = globalConfig()
auxdir = 'auxiliary'
indir = "EODP_TER/EODP-TS-L1C/input"
outdir = "EODP_TER/EODP-TS-L1C/output"
outrefdir = "EODP_TER/EODP-TS-L1C/output_ref"

# PASS/FAIL Criteria 1
for band in globalConfig.bands:
    try:
        toa = np.sort(readToa(outdir, globalConfig.l1c_toa + band + '.nc'))
        toa_ref = np.sort(readToa(outrefdir, globalConfig.l1c_toa + band + '.nc'))
        # Set to 0 negative values
        toa[toa<0] = 0
        toa_ref[toa_ref < 0] = 0
        error = np.divide(np.abs(toa-toa_ref), toa, out=np.zeros_like(toa), where=toa != 0)*100 # Div handling div/0
        assert (error < 0.01).sum() > toa_ref.size*0.997
        print(f'PASSED for {band}')
    except AssertionError as e:
        print(f'TEST failed for band: {band}. Points exceeding 0.01 deviation: {(error > 0.01).sum()} of {toa_ref.size-toa_ref.size*0.997} allowed')

