import pandas as pd
data = [10, 20, 30, 40, 50, 60]
index = pd.MultiIndex.from_tuples([('A', 1), ('A', 2), ('B', 1), ('B', 2), ('C', 1), ('C', 2)])
series = pd.Series(data, index=index)
print("Series with MultiIndex:")
print(series)
subset_A = series.loc['A']
print("\nSubset A:")
print(subset_A)
subset_A_inner_2 = series.loc[('A', 2)]
print("\nSubset A, Inner 2:")
print(subset_A_inner_2)
subset_B = series.loc['B']
print("\nSubset B:")
print(subset_B)
subset_C_inner_1 = series.loc[('C', 1)]
print("\nSubset C, Inner 1:")
print(subset_C_inner_1)
subset_B_xs = series.xs('B')
print("\nSubset B using xs:")
print(subset_B_xs)
subset_inner_2 = series.xs(2, level=1)
print("\nSubset Inner Level 2 using xs:")
print(subset_inner_2)
