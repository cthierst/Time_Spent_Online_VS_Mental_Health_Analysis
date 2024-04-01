# Placeholder Title

## Overview
This repository contains all files necessary to conduct an analysis on the Ontarian population's mental health status in relation to rate of internet usage. The aim of this analysis is to determine if increased internet use influences mental health status. It also considers gender and visible minority identity. 

## Requirements

This analysis requires Python and SPSS. To complete this project you will need to have software that is capable of running both program types. Additionally this project is dependent on several libraries to function. These libraries include:

- pandas
- sklearn
- matplotlib
- package
- package
- seaborn
- plotly
- mord

To install these libraries, use the following command replacing '[package name]'  with the necessary package above:

pip install [package name]

## Downloading Data
The data for this paper comes from Statistics Canada's 2020 Canadian Internet Use Survey. To access this data you will need to download it first from their webiste then use SPSS to open and save the data as a CSV file.

The raw data for this project can be found in the CIUS_2020_raw.csv file.

## Cleaning Data
The data was cleaned using python to filter for relevant variables to the study. Values were adjusted to help with human-readability and outliers and instances of missing data were removed. This resulted in two versions of our cleaned data CSV file, one for variable measuring and one to assist in cluster analysis.

The PY files for cleaning can be found in 
- Data_Cleaning.py
- Data_Cleaning_Numbers.py

The resulting clean CSV files can be found in
- filtered_clean_df.csv
- filtered_clean_numeric_df.csv

## Analyzing Data
Data analysis included descriptive and non-parametric testing and modelling:
- Descriptive statistics
- Chi-Squared Tests
- Logistic Regression
- Cluster Analysis

These files can be found:
- Graphing_Analyses.py
- ChiSquare_Tests.py
- Logistic_Regression.py
- Cluster_Analysis.py 

## Notes
To run this code we recommend downloading and saving all of these files to one folder and then open that folder to run the programs. 



