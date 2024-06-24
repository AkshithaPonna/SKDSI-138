import pandas as pd
import matplotlib.pyplot as plt

# Data for the plots
data_dict = {
    'Cat_A': [4, 7, 1, 8, 5],
    'Cat_B': [5, 2, 8, 3, 6],
    'Cat_C': [7, 5, 3, 4, 9]
}
index_labels = ['Item1', 'Item2', 'Item3', 'Item4', 'Item5']
data_frame = pd.DataFrame(data_dict, index=index_labels)

# Side-by-side bar plot
axis1 = data_frame.plot(kind='bar', figsize=(10, 6))
axis1.set_xlabel('Items')
axis1.set_ylabel('Values')
axis1.set_title('Side-by-Side Bar Plot')
plt.xticks(rotation=0)
plt.show()

# Stacked bar plot
axis2 = data_frame.plot(kind='bar', stacked=True, figsize=(10, 6))
axis2.set_xlabel('Items')
axis2.set_ylabel('Values')
axis2.set_title('Stacked Bar Plot')
plt.xticks(rotation=0)
plt.show()
