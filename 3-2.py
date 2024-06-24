import pandas as pd

# Using Start date and End date
start_date = '2024-01-01'
end_date = '2024-12-31'
date_range_1 = pd.date_range(start=start_date, end=end_date)
print(date_range_1)

# Using Start date and Periods
start_date = '2024-01-01'
num_periods = 365  # for a full year
date_range_2 = pd.date_range(start=start_date, periods=num_periods)
print(date_range_2)

# Using End date and Periods
end_date = '2024-12-31'
num_periods = 365  # for a full year
date_range_3 = pd.date_range(end=end_date, periods=num_periods)
print(date_range_3)

# Using Frequency
start_date = '2024-01-01'
end_date = '2024-12-31'
date_range_4 = pd.date_range(start=start_date, end=end_date, freq='D') # 'D' generates dates on daily basis
print(date_range_4)
