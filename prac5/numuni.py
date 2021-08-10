import numpy as np
array1 = np.array([0, 11, 21, 41, 61, 91])
print("Array1: ",array1)
array2 = [5, 31, 9, 51, 71]
print("Array2: ",array2)
print("Unique sorted array of values that are in either of the two input arrays:")
print(np.union1d(array1, array2))