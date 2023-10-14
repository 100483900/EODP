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
#outeqoffdir = "EODP_TER/EODP-TS-ISM/output_eqoff"
outrefdir = "EODP_TER/EODP-TS-ISM/output_ref"

# PASS/FAIL Criteria 1 ISRF
for band in globalConfig.bands:
    try:
        toa = readToa(outdir, globalConfig.ism_toa_isrf + band + '.nc')
        toa_ref = readToa(outrefdir, globalConfig.ism_toa_isrf + band + '.nc')
        error = np.divide(np.abs(toa-toa_ref), toa, out=np.zeros_like(toa), where=toa != 0)*100 # Div handling div/0
        assert (error < 0.01).sum() > toa_ref.size*0.997
        print(f'PASSED for {band}')
    except AssertionError as e:
        print(f'TEST failed for band: {band}. Points exceeding 0.01 deviation: {(error > 0.01).sum()} of {toa_ref.size-toa_ref.size*0.997} allowed')

# PASS/FAIL Criteria 2 OPTICAL
for band in globalConfig.bands:
    try:
        toa = readToa(outdir, globalConfig.ism_toa_optical + band + '.nc')
        toa_ref = readToa(outrefdir, globalConfig.ism_toa_optical + band + '.nc')
        error = np.divide(np.abs(toa-toa_ref), toa, out=np.zeros_like(toa), where=toa != 0)*100 # Div handling div/0
        assert (error < 0.01).sum() > toa_ref.size * 0.997
        print(f'PASSED for {band}')
    except AssertionError as e:
        print(
            f'TEST failed for band: {band}. Points exceeding 0.01 deviation: {(error > 0.01).sum()} of {toa_ref.size - toa_ref.size * 0.997} allowed')

# PASS/FAIL Criteria 2 and 3
    try:
        toa = readToa(outdir, globalConfig.l1b_toa + band + '.nc')
        ism_toa_isrf = readToa(indir, globalConfig.ism_toa_isrf + band + '.nc')
        toa_eqoff = readToa(outeqoffdir, globalConfig.l1b_toa + band + '.nc')

        central_ALT_toa = toa[int(toa.shape[0]/2),:]
        central_ALT_ism_toa_isrf = ism_toa_isrf[int(ism_toa_isrf.shape[0] / 2), :]
        central_ALT_toa_eqoff = toa_eqoff[int(toa_eqoff.shape[0] / 2), :]

        # Plot
        plt.title("Line graph")
        plt.plot(central_ALT_toa, color="black")
        plt.plot(central_ALT_ism_toa_isrf, color="blue")
        plt.plot(central_ALT_toa_eqoff, color="red")
        plt.legend(["TOA L1B with equalizer", "TOA L1B ISRF", "TOA L1B no equalizer"], loc="lower right")
        plt.xlabel("ACT pixel [-]")
        plt.ylabel("TOA [mW/m2/sr]")
        plt.title(f'Effect of the Equalization for {band}')
        plt.grid()
        plt.show()

    except AssertionError as e:
        print()


#python find = argwhere