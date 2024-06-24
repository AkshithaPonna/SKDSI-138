import pandas as pd

# Define the start and end dates
start_date = '2024-01-01'
end_date = '2024-01-05'

# Create a date range with UTC timezone
date_range_utc = pd.date_range(start=start_date, end=end_date, freq='D', tz='UTC')
print("UTC Timezone Date Range:")
print(date_range_utc)

# Create a date range without timezone and then localize it to 'America/New_York'
date_range_ny = pd.date_range(start=start_date, end=end_date, freq='D')
date_range_ny = date_range_ny.tz_localize('America/New_York')
print("\nLocalized to America/New_York Timezone:")
print(date_range_ny)

# Convert the 'America/New_York' localized date range to 'Europe/London' timezone
date_range_london = date_range_ny.tz_convert('Europe/London')
print("\nConverted to Europe/London Timezone:")
print(date_range_london)

# Create two different date ranges with different timezones
date_range1 = pd.date_range(start=start_date, periods=3, freq='D', tz='UTC')
date_range2 = pd.date_range(start=start_date, periods=3, freq='D', tz='America/New_York')

# Combine the two different timezone date ranges
combined_date_range = date_range1.union(date_range2)
print("\nCombined Date Ranges with Different Timezones:")
print(combined_date_range)
