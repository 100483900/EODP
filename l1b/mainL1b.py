
# MAIN FUNCTION TO CALL THE L1B MODULE

from l1b.src.l1b import l1b
import os


# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = 'auxiliary'
indir = "EODP_TER/EODP-TS-L1B/input"
outdir = "EODP_TER/EODP-TS-L1B/output"
input_e2e = "EODP_TER/EODP-TS-E2E/outputISM"
output_e2e = "EODP_TER/EODP-TS-E2E/outputL1b"

# Initialise the ISM
myL1b = l1b(auxdir, input_e2e, output_e2e)
myL1b.processModule()
