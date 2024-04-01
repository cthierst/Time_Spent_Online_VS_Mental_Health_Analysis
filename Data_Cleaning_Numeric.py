# Purpose: The purpose of this code is to create the graphical visualizations for our INF412 final project.
# Authors: Chloe Thierstein, Sebastian Rodriguez, Laura Lee-Chu, Yixin Fan
# Contact: chloe.thierstein@mail.utoronto.ca 
# Date: March 31, 2024 

# Imports necessary libraries
import pandas as pd

# Imports the data clean and filtered data frame
df = pd.read_csv("filtered_clean_df.csv", low_memory=False)

# Drops the Province columns
df = df.drop('Province', axis=1)

# Converts gender to numeric values
df['Gender'].replace("Male", 1, inplace=True)
df['Gender'].replace("Female", 2, inplace=True)

# Cleans time using the internet column variables for cluster analysis
df['Time spent using the internet'].replace("None", 1, inplace=True)
df['Time spent using the internet'].replace("Less than 5 hours/week", 2, inplace=True)
df['Time spent using the internet'].replace("5 to less than 10 hours/week", 3, inplace=True)
df['Time spent using the internet'].replace("10 to less than 20 hours/week", 4, inplace=True)
df['Time spent using the internet'].replace("20 to less than 40 hours/week", 5, inplace=True)
df['Time spent using the internet'].replace("40 hours+/week", 6, inplace=True)
df['Time spent using the internet'].replace("Valid skip", 96, inplace=True)
df['Time spent using the internet'].replace("Not Stated", 99, inplace=True)

# Cleans relationship satisfaction: friends column variables for cluster analysis
df['Relationship Sat: Friends'].replace("Completely dissatisfied", 1, inplace=True)
df['Relationship Sat: Friends'].replace("Somewhat dissatisfied", 2, inplace=True)
df['Relationship Sat: Friends'].replace("Neither satisfied nor dissatisfied", 3, inplace=True)
df['Relationship Sat: Friends'].replace("Somewhat satisfied", 4, inplace=True)
df['Relationship Sat: Friends'].replace("Completely satisfied", 5, inplace=True)
df['Relationship Sat: Friends'].replace("Valid Skip", 6, inplace=True)
df['Relationship Sat: Friends'].replace("Not Stated", 9, inplace=True)

# Cleans relationship satisfaction: relatives or family not living with column variables for cluster analysis
df['Relationship Sat: Relatives or family not living with'].replace("Completely dissatisfied", 1, inplace=True)
df['Relationship Sat: Relatives or family not living with'].replace("Somewhat dissatisfied", 2, inplace=True)
df['Relationship Sat: Relatives or family not living with'].replace("Neither satisfied nor dissatisfied", 3, inplace=True)
df['Relationship Sat: Relatives or family not living with'].replace("Somewhat satisfied", 4, inplace=True)
df['Relationship Sat: Relatives or family not living with'].replace("Completely satisfied", 5, inplace=True)
df['Relationship Sat: Relatives or family not living with'].replace("Valid Skip", 6, inplace=True)
df['Relationship Sat: Relatives or family not living with'].replace("Not Stated", 9, inplace=True)

# # Cleans life satisfaction column variables for cluster analysis
df['Life Satisfaction'].replace("Very Dissatisfied", 1, inplace=True)
df['Life Satisfaction'].replace("Quite Dissatisfied", 2, inplace=True)
df['Life Satisfaction'].replace("Moderately Dissatisfied", 3, inplace=True)
df['Life Satisfaction'].replace("Somewhat Dissatisfied", 4, inplace=True)
df['Life Satisfaction'].replace("Slightly Dissatisfied", 5, inplace=True)
df['Life Satisfaction'].replace("Neither Satisfied nor Dissatisfied", 6, inplace=True)
df['Life Satisfaction'].replace("Slightly Satisfied", 7, inplace=True)
df['Life Satisfaction'].replace("Somewhat Satisfied", 8, inplace=True)
df['Life Satisfaction'].replace("Moderately Satisfied", 9, inplace=True)
df['Life Satisfaction'].replace("Quite Satisfied", 10, inplace=True)
df['Life Satisfaction'].replace("Very Satisfied", 11, inplace=True)
df['Life Satisfaction'].replace("Not Stated", 99, inplace=True)

# Cleans perceived mental health column variables for cluster analysis
df['Perceived Mental Health'].replace("Excellent", 1, inplace=True)
df['Perceived Mental Health'].replace("Very Good", 2, inplace=True)
df['Perceived Mental Health'].replace("Good", 3, inplace=True)
df['Perceived Mental Health'].replace("Fair", 4, inplace=True)
df['Perceived Mental Health'].replace("Poor", 5, inplace=True)
df['Perceived Mental Health'].replace("Not stated", 9, inplace=True)

# Cleans visible minority column variables for cluster analysis
df['Visible Minority'].replace("Visible minority", 1, inplace=True)
df['Visible Minority'].replace("Non-visible minority", 2, inplace=True)
df['Visible Minority'].replace("Not stated", 9, inplace=True)

# Drosp rows with missing values in specific columns
df.dropna(subset=['Time spent using the internet'], inplace=True)
df.dropna(subset=['Life Satisfaction'], inplace=True)
df.dropna(subset=['Visible Minority'], inplace=True)

# Saves the cleaned and filtered nueric dataframe to a new csv to be used in our cluster analysis
df.to_csv('filtered_clean_numeric_df.csv', index=False)