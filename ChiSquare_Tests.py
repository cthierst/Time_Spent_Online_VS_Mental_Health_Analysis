# Purpose: The purpose of this code is to perform chi-square tests for our INF412 final project.
# Authors: Chloe Thierstein, Sebastian Rodriguez, Laura Lee-Chu, Yixin Fan
# Contact: chloe.thierstein@mail.utoronto.ca 
# Date: March 31, 2024  

# Imports all of the necessary libraries
import pandas as pd
from scipy.stats import chi2_contingency

# Imports the clean and filtered data frame
df = pd.read_csv("filtered_clean_df.csv", low_memory=False)

## PERCEIVED MENTAL HEALTH VS. TIME SPENT USING THE INTERNET ##

# Creates a contingency table
contingency_table = pd.crosstab(index=df['Perceived Mental Health'], columns=df['Time spent using the internet'])

# Performs the chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Displays the results
print("Contingency Table:")
print(contingency_table)
print("\nChi-square statistic:", chi2)
print("p-value:", p)
print("Degrees of freedom:", dof)
print("Expected frequencies table:")
print(expected)

# Automatically interprets the results
if p < 0.05:
    print("\nSince the p-value is less than 0.05, we reject the null hypothesis.")
    print("There is significant evidence to suggest that there is an association between Perceived Mental Health and Time spent using the internet.")
else:
    print("\nThe p-value is greater than 0.05, so we fail to reject the null hypothesis.")
    print("There is no significant evidence to suggest an association between Perceived Mental Health and Time spent using the internet.")

## GENDER VS. TIME SPENT USING THE INTERNET ##
    
# Creates a contingency table
contingency_table = pd.crosstab(index=df['Gender'], columns=df['Time spent using the internet'])

# Performs the chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Displays the results
print("Contingency Table:")
print(contingency_table)
print("\nChi-square statistic:", chi2)
print("p-value:", p)
print("Degrees of freedom:", dof)
print("Expected frequencies table:")
print(expected)

# Automatically interprets the results
if p < 0.05:
    print("\nSince the p-value is less than 0.05, we reject the null hypothesis.")
    print("There is significant evidence to suggest that there is an association between Gender and Time spent using the internet.")
else:
    print("\nThe p-value is greater than 0.05, so we fail to reject the null hypothesis.")
    print("There is no significant evidence to suggest an association between Gender and Time spent using the internet.")

## VISIBLE MINORITY VS. TIME SPENT USING THE INTERNET ##

# Creates a contingency table
contingency_table = pd.crosstab(index=df['Visible Minority'], columns=df['Time spent using the internet'])

# Performs the chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Displays the results
print("Contingency Table:")
print(contingency_table)
print("\nChi-square statistic:", chi2)
print("p-value:", p)
print("Degrees of freedom:", dof)
print("Expected frequencies table:")
print(expected)

# Automatically interprets the results
if p < 0.05:
    print("\nSince the p-value is less than 0.05, we reject the null hypothesis.")
    print("There is significant evidence to suggest that there is an association between Visible Minority and Time spent using the internet.")
else:
    print("\nThe p-value is greater than 0.05, so we fail to reject the null hypothesis.")
    print("There is no significant evidence to suggest an association between Visible Minority and Time spent using the internet.")

## LIFE SATISFACTION VS. TIME SPENT USING THE INTERNET ##

# Creates a contingency table
contingency_table = pd.crosstab(index=df['Life Satisfaction'], columns=df['Time spent using the internet'])

# Performs the chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Displays the results
print("Contingency Table:")
print(contingency_table)
print("\nChi-square statistic:", chi2)
print("p-value:", p)
print("Degrees of freedom:", dof)
print("Expected frequencies table:")
print(expected)

# Automatically interprets the results
if p < 0.05:
    print("\nSince the p-value is less than 0.05, we reject the null hypothesis.")
    print("There is significant evidence to suggest that there is an association between Life Satisfaction and Time spent using the internet.")
else:
    print("\nThe p-value is greater than 0.05, so we fail to reject the null hypothesis.")
    print("There is no significant evidence to suggest an association between Life Satisfaction and Time spent using the internet.")

## FRIENDSHIP RELATIONSHIP SATISFACTION VS TIME SPENT ON THE INTERNET ##
    
# Creates a contingency table
contingency_table = pd.crosstab(index=df['Relationship Sat: Friends'], columns=df['Time spent using the internet'])

# Performs the chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Displays the results
print("Contingency Table:")
print(contingency_table)
print("\nChi-square statistic:", chi2)
print("p-value:", p)
print("Degrees of freedom:", dof)
print("Expected frequencies table:")
print(expected)

# Automatically interprets the results
if p < 0.05:
    print("\nSince the p-value is less than 0.05, we reject the null hypothesis.")
    print("There is significant evidence to suggest that there is an association between Relationship Sat: Friends and Time spent using the internet.")
else:
    print("\nThe p-value is greater than 0.05, so we fail to reject the null hypothesis.")
    print("There is no significant evidence to suggest an association between Relationship Sat: Friends and Time spent using the internet.")

## FAMILY RELATIONSHIP SATISFACTION VS TIME SPENT ON THE INTERNET ##
    
# Creates a contingency table
contingency_table = pd.crosstab(index=df['Relationship Sat: Relatives or family not living with'], columns=df['Time spent using the internet'])

# Performs the chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)

# Displays the results
print("Contingency Table:")
print(contingency_table)
print("\nChi-square statistic:", chi2)
print("p-value:", p)
print("Degrees of freedom:", dof)
print("Expected frequencies table:")
print(expected)

# Automatically interprets the results
if p < 0.05:
    print("\nSince the p-value is less than 0.05, we reject the null hypothesis.")
    print("There is significant evidence to suggest that there is an association between Relationship Sat: Relatives or family not living with and Time spent using the internet.")
else:
    print("\nThe p-value is greater than 0.05, so we fail to reject the null hypothesis.")
    print("There is no significant evidence to suggest an association between Relationship Sat: Relatives or family not living with and Time spent using the internet.")