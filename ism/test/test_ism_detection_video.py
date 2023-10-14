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
