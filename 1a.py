import pandas as pd
import numpy as np

# Initial data
data_dict = {
    'Col1': [1, 2, np.nan, 4, 5, np.nan, 7],
    'Col2': [np.nan, 2, 3, 4, np.nan, 6, 7],
    'Col3': ['foo', 'bar', 'baz', np.nan, 'qux', 'quux', 'corge'],
    'Col4': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
}

# Creating DataFrame
data_frame = pd.DataFrame(data_dict)
print("Original DataFrame:")
print(data_frame)

# Finding missing data
missing_data_frame = data_frame.isna()
print("\nMissing Data in DataFrame:")
print(missing_data_frame)

# Dropping rows with any missing data
data_frame_dropna_rows = data_frame.dropna()
print("\nDataFrame after dropping rows with any missing data:")
print(data_frame_dropna_rows)

# Dropping columns with any missing data
data_frame_dropna_cols = data_frame.dropna(axis=1)
print("\nDataFrame after dropping columns with any missing data:")
print(data_frame_dropna_cols)

# Filling missing data with specific values
data_frame_fillna = data_frame.fillna(value={
    'Col1': data_frame['Col1'].mean(), 
    'Col2': data_frame['Col2'].mean(), 
    'Col3': 'missing', 
    'Col4': 0
})
print("\nDataFrame after filling missing data:")
print(data_frame_fillna)

# Adding a duplicate row
data_frame_with_duplicates = data_frame.append(data_frame.iloc[2], ignore_index=True)
print("\nDataFrame with Duplicates:")
print(data_frame_with_duplicates)

# Finding duplicates
duplicates_frame = data_frame_with_duplicates.duplicated()
print("\nDuplicates in DataFrame:")
print(duplicates_frame)

# Removing duplicates
data_frame_no_duplicates = data_frame_with_duplicates.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(data_frame_no_duplicates)
