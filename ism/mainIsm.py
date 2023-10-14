
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism
import os

auxdir = 'auxiliary'
indir = "EODP_TER/EODP-TS-ISM/input/gradient_alt100_act150"
outdir = "EODP_TER/EODP-TS-ISM/output"

# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
