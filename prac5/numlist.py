import numpy as np
import pandas as pd
np_array = np.array([11, 21, 31, 41, 51])
print("NumPy array:")
print(np_array)
new_series = pd.Series(np_array)
print("Converted Pandas series:")
print(new_series)