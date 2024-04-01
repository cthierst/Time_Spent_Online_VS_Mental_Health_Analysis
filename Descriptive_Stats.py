# Purpose: The purpose of this code is to define all of the possible descriptive statistics based on our dataset for our INF412 final project.
# Authors: Chloe Thierstein, Sebastian Rodriguez, Laura Lee-Chu, Yixin Fan
# Contact: chloe.thierstein@mail.utoronto.ca 
# Date: March 31, 2024 

# Imports all of the necessary libraries
import pandas as pd

# Imports the data clean and filtered data frame
df = pd.read_csv("filtered_clean_df.csv")

# Computes the descriptive statistics
descriptive_stats = df.describe(include='all').transpose()

# Renames the index to 'variable' for easier readability
descriptive_stats = descriptive_stats.rename_axis('variable')

# Displays the descriptive statistics
print(descriptive_stats)

# Saves the descriptive statistics to a CSV file for easier finding
descriptive_stats.to_csv('Descriptive_Statistics.csv')
