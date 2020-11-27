"""
Compressive Sensing Practice coding
"""

import numpy as np
# measurements, unknowns, sparsity. n>>m
m, n, k = 100, 20, 3

# Create GRN populated matrix
A = np.random.normal(size = (m,n))
# Create some measurement vector y
# with appropriate size since x is nx1
y = np.random.exponential(size = m)

pf = 1 # penalty factor lambda
# Once we have A and y
# Write function
# Minmize this function for lowest k x values



# Try using lasso code here
print(x)