
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism
import os

auxdir = 'auxiliary'
indir = "EODP_TER/EODP-TS-ISM/input/gradient_alt100_act150"
indir_e2e = "EODP_TER/EODP-TS-E2E/sgm_out"
outdir_e2e = "EODP_TER/EODP-TS-E2E/output"
outdir = "EODP_TER/EODP-TS-ISM/output"

# Initialise the ISM
myIsm = ism(auxdir, indir_e2e, outdir)
myIsm.processModule()
