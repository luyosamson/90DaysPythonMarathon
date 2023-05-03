#  NumPy: NumPy is a popular package used for numerical computing in Python.
#  It provides tools for working with arrays and matrices,
#  and includes functions for mathematical operations such as linear algebra
#  and Fourier analysis.

import numpy as np
arr=np.array([2,6,8,4,2])
mean=np.mean(arr)
std_dev=np.std(arr)
print("The mean is",mean)
print("Standard deviation is ",std_dev)