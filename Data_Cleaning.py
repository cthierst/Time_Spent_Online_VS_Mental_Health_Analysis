# Purpose: The purpose of this code is to perform the initial data cleaning for our INF412 final project.
# Authors: Chloe Thierstein, Sebastian Rodriguez, Laura Lee-Chu, Yixin Fan
# Contact: chloe.thierstein@mail.utoronto.ca 
# Date: March 31, 2024 

# Imports necessary libraries
import pandas as pd

# Loads in the raw CIUS 2020 data
df = pd.read_csv("CIUS_2020_raw.csv", low_memory=False)

# Drops unnecessary columns
clean_df = df[["PROVINCE", "GENDER", "UI_060A", "TS_010A", "TS_010B", "FD_020A", "FD_030A", "G_VISMIN"]]

# Checks to ensure only selected columns remain
print(clean_df)

## Column Cleaning ##

# Create copy of the dataframe to avoid ambiguity 
clean_df = clean_df.copy()

# Cleans province column title
clean_df.rename(columns = {'PROVINCE': 'Province'}, inplace=True)

# Cleans province column variables
clean_df["Province"].replace(10, "Newfoundland and Labrador", inplace=True)
clean_df["Province"].replace(11, "Prince Edward Island", inplace=True)
clean_df["Province"].replace(12, "Nova Scotia", inplace=True)
clean_df["Province"].replace(13, "New Brunswick", inplace=True)
clean_df["Province"].replace(24, "Quebec", inplace=True)
clean_df["Province"].replace(35, "Ontario", inplace=True)
clean_df["Province"].replace(46, "Manitoba", inplace=True)
clean_df["Province"].replace(47, "Saskatchewan", inplace=True)
clean_df["Province"].replace(48, "Alberta", inplace=True)
clean_df["Province"].replace(59, "British Columbia", inplace=True)
clean_df["Province"].replace(96, "Valid Skip", inplace=True)
clean_df["Province"].replace(97, "Don't Know", inplace=True)
clean_df["Province"].replace(98, "Refusal", inplace=True)
clean_df["Province"].replace(99, "Not Stated", inplace=True)

# Cleans gender column title
clean_df.rename(columns = {'GENDER': 'Gender'}, inplace=True)

# Cleans gender column variables
clean_df["Gender"].replace(1, "Male", inplace=True)
clean_df["Gender"].replace(2, "Female", inplace=True)

# Cleans time using the internet column title
clean_df.rename(columns = {'UI_060A': 'Time spent using the internet'}, inplace=True)

# Cleans time using the internet column variables
clean_df['Time spent using the internet'].replace(1, "None", inplace=True)
clean_df['Time spent using the internet'].replace(2, "Less than 5 hours/week", inplace=True)
clean_df['Time spent using the internet'].replace(3, "5 to less than 10 hours/week", inplace=True)
clean_df['Time spent using the internet'].replace(4, "10 to less than 20 hours/week", inplace=True)
clean_df['Time spent using the internet'].replace(5, "20 to less than 40 hours/week", inplace=True)
clean_df['Time spent using the internet'].replace(6, "40 hours+/week", inplace=True)
clean_df['Time spent using the internet'].replace(96, "Valid skip", inplace=True)
clean_df['Time spent using the internet'].replace(99, "Not Stated", inplace=True)

# Cleans relationship satisfaction: friends column title
clean_df.rename(columns = {'TS_010A':'Relationship Sat: Friends'}, inplace=True)

# Cleans relationship satisfaction: friends column variables
clean_df['Relationship Sat: Friends'].replace(1, "Completely dissatisfied", inplace=True)
clean_df['Relationship Sat: Friends'].replace(2, "Somewhat dissatisfied", inplace=True)
clean_df['Relationship Sat: Friends'].replace(3, "Neither satisfied nor dissatisfied", inplace=True)
clean_df['Relationship Sat: Friends'].replace(4, "Somewhat satisfied", inplace=True)
clean_df['Relationship Sat: Friends'].replace(5, "Completely satisfied", inplace=True)
clean_df['Relationship Sat: Friends'].replace(6, "Valid Skip", inplace=True)
clean_df['Relationship Sat: Friends'].replace(9, "Not Stated", inplace=True)

# Cleans relationship satisfaction: relatives or family not living with column title
clean_df.rename(columns = {'TS_010B':'Relationship Sat: Relatives or family not living with'}, inplace=True)

# Cleans relationship satisfaction: relatives or family not living with column variables
clean_df['Relationship Sat: Relatives or family not living with'].replace(1, "Completely dissatisfied", inplace=True)
clean_df['Relationship Sat: Relatives or family not living with'].replace(2, "Somewhat dissatisfied", inplace=True)
clean_df['Relationship Sat: Relatives or family not living with'].replace(3, "Neither satisfied nor dissatisfied", inplace=True)
clean_df['Relationship Sat: Relatives or family not living with'].replace(4, "Somewhat satisfied", inplace=True)
clean_df['Relationship Sat: Relatives or family not living with'].replace(5, "Completely satisfied", inplace=True)
clean_df['Relationship Sat: Relatives or family not living with'].replace(6, "Valid Skip", inplace=True)
clean_df['Relationship Sat: Relatives or family not living with'].replace(9, "Not Stated", inplace=True)

# Cleans life satisfaction column title
clean_df.rename(columns = {'FD_020A':'Life Satisfaction'}, inplace=True)

# Cleans life satisfaction column variables
clean_df['Life Satisfaction'].replace(1, "Very Dissatisfied", inplace=True)
clean_df['Life Satisfaction'].replace(2, "Quite Dissatisfied", inplace=True)
clean_df['Life Satisfaction'].replace(3, "Moderately Dissatisfied", inplace=True)
clean_df['Life Satisfaction'].replace(4, "Somewhat Dissatisfied", inplace=True)
clean_df['Life Satisfaction'].replace(5, "Slightly Dissatisfied", inplace=True)
clean_df['Life Satisfaction'].replace(6, "Neither Satisfied nor Dissatisfied", inplace=True)
clean_df['Life Satisfaction'].replace(7, "Slightly Satisfied", inplace=True)
clean_df['Life Satisfaction'].replace(8, "Somewhat Satisfied", inplace=True)
clean_df['Life Satisfaction'].replace(9, "Moderately Satisfied", inplace=True)
clean_df['Life Satisfaction'].replace(10, "Quite Satisfied", inplace=True)
clean_df['Life Satisfaction'].replace(11, "Very Satisfied", inplace=True)
clean_df['Life Satisfaction'].replace(99, "Not Stated", inplace=True)

# Cleans perceived mental health column title
clean_df.rename(columns = {'FD_030A':'Perceived Mental Health'}, inplace=True)

# Cleans perceived mental health column variables
clean_df['Perceived Mental Health'].replace(1, "Excellent", inplace=True)
clean_df['Perceived Mental Health'].replace(2, "Very Good", inplace=True)
clean_df['Perceived Mental Health'].replace(3, "Good", inplace=True)
clean_df['Perceived Mental Health'].replace(4, "Fair", inplace=True)
clean_df['Perceived Mental Health'].replace(5, "Poor", inplace=True)
clean_df['Perceived Mental Health'].replace(9, "Not stated", inplace=True)

# Cleans visible minority column title
clean_df.rename(columns = {'G_VISMIN':'Visible Minority'}, inplace=True)

# Cleans visible minority column variables
clean_df['Visible Minority'].replace(1, "Visible minority", inplace=True)
clean_df['Visible Minority'].replace(2, "Non-visible minority", inplace=True)
clean_df['Visible Minority'].replace(9, "Not stated", inplace=True)

# Checks to make sure the data has been appropriately cleaned
print(clean_df)

## Removing rows to ensure we are only looking at data from Ontarian respondents ##

# Converts the Province column to categorical
clean_df['Province'] = pd.Categorical(clean_df['Province'])

# Defines the list of provinces that are not Ontario
filter_values = ['Alberta', 'Manitoba', 'Saskatchewan', 'British Columbia', 'Not Stated', 'Prince Edward Island', "New Brunswick", 'Nova Scotia', 'Quebec', 'Newfoundland and Labrador']

# Filters our any rows that do not include Ontario
clean_df = clean_df[~clean_df['Province'].isin(filter_values)]

# Displays the filtered data frame to check for mistakes
print(clean_df)

## Removing not stated or skipped responses ##

# Filters out the "Not Stated" or "Valid Skip" responses
valid_responses = ['Not Stated', 'Valid Skip', 'Not stated', 'Valid skip']
clean_df = clean_df[~clean_df.apply(lambda row: row.astype(str).str.contains('|'.join(valid_responses)).any(), axis=1)]

## Checking for missing values ##

# Checks for missing values
print(clean_df.isnull().sum())

# Saves the final filtered and cleaned data frame to be used in analyses 
clean_df.to_csv('filtered_clean_df.csv', index=False)