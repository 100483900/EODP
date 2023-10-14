
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism
import os

auxdir = 'auxiliary'
indir = "EODP_TER/EODP-TS-ISM/input"
outdir = "EODP_TER/EODP-TS-ISMoutput"

# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
