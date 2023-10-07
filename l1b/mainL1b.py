
# MAIN FUNCTION TO CALL THE L1B MODULE

from l1b.src.l1b import l1b
import os


# Directory - this is the common directory for the execution of the E2E, all modules
ROOT_DIR = '../'
auxdir = os.path.join(ROOT_DIR, 'auxiliary')
indir = os.path.join(ROOT_DIR, "EODP_TER/EODP-TS-L1B/input")
outdir = os.path.join(ROOT_DIR, "EODP_TER/EODP-TS-L1B/output")

# Initialise the ISM
myL1b = l1b(auxdir, indir, outdir)
myL1b.processModule()
