#!/usr/bin/python3

from scipy.linalg import eig, pinv, norm

import numpy as np

W = np.matrix([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
l = np.real(eig(W, right=False))

Psi = np.vander(l, N=2, increasing=True)

v = np.matrix(np.random.randn(2, 1))
assert norm(pinv(Psi) * (Psi * v) - v) < 1e-10

# r0.T * v; Psi00 * v0 + Psi01 * v1
# r1.T * v; Psi10 * v0 + Psi11 * v1
# r2.T * v; Psi20 * v0 + Psi21 * v1

# v0 * c0 + v1 * c1

# Psi10 * v0 + Psi11 * v1 = 0
# Psi20 * v0 + Psi21 * v1 = 0

# v0 = -Psi11 / Psi10 * v1 -> for the W and Psi above, Psi[1,1] is 0.
# v0 = -Psi21 / Psi20 * v1

v1 = np.random.randn(1)
v0 = -Psi[2, 1] / Psi[2, 0] * v1

h = np.matrix([v0, v1])
g = Psi * h
assert norm(h - pinv(Psi) * g) < 1e-10

print(g)

# In the example above we have arrived at a condition for generating
# 2D vectors v such that their projection via Psi renders a 3D vector
# whose last element is zero. We have also seen that the only 2D vector
# whose projection via Psi renders a 3D vector whose last two elements
# are zero is the null vector.

# The system is homogeneus, coefficient and extended matrices are rank 2.
# What are the systems that would give inifinite number of solutions to
# say get vectors in the large/frequency domain that are bandpass?
