import pandas as pd
d1 = {'a': 101, 'b': 201, 'c':301, 'd':401, 'e':501}
print("Original dictionary:")
print(d1)
new_series = pd.Series(d1)
print("Converted series:")
print(new_series)