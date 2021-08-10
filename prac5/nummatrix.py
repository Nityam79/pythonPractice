import pandas as pd
ds1 = pd.Series([12, 14, 16, 18 ])
ds2 = pd.Series([11, 13, 15, 17])
ds = ds1 + ds2
print("Add two Series:")
print(ds)
print("Subtract two Series:")
ds = ds1 - ds2
print(ds)
print("Multiply two Series:")
ds = ds1 * ds2
print(ds)
print("Divide Series1 by Series2:")
ds = ds1 / ds2
print(ds)