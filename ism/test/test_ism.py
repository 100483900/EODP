import logging

from common.io.writeToa import readToa
import numpy as np
from config.globalConfig import globalConfig
import os
import matplotlib.pyplot as plt


# Inits
globalConfig = globalConfig()
auxdir = 'auxiliary'
indir = "EODP_TER/EODP-TS-L1B/input"
outdir = "EODP_TER/EODP-TS-L1B/output"
outeqoffdir = "EODP_TER/EODP-TS-L1B/output_eqoff"
outrefdir = "EODP_TER/EODP-TS-L1B/output_ref"
