
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism
import os

# Directory - this is the common directory for the execution of the E2E, all modules
ROOT_DIR = '../'
auxdir = os.path.join(ROOT_DIR, 'auxiliary')
indir = os.path.join(ROOT_DIR, "EODP_TER/EODP-TS-ISM/input")
outdir = os.path.join(ROOT_DIR, "EODP_TER/EODP-TS-ISMoutput")

# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
