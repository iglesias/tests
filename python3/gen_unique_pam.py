#!/usr/bin/python3
""" Sample little program showcasing command line usage and saving numpy matrices"""

import subprocess
import numpy as np

NUM_ROWS = 216
NUM_COLS = 144
NUM_CELLS = NUM_ROWS * NUM_COLS

for frame in range(30, 10 + 1):
    probs = np.zeros(NUM_CELLS)
    cmd = ["""/bin/grep ' 04 ' pam-f%d.dat""" % frame]
    outcmd = subprocess.getoutput(cmd).split()
    idxs = [i for i, x in enumerate(outcmd) if x == '04']
    for idx in idxs:
        probs[int(outcmd[idx - 1])] = float(outcmd[idx + 1])

    np.savetxt(
        'pam-04-f%d.dat' % frame,
        np.stack((np.arange(NUM_CELLS), probs), axis=1),
        fmt='%d %.4f')
