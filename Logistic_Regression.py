# Purpose: The purpose of this code is to perform a logistic regression for our INF412 final project.
# Authors: Chloe Thierstein, Sebastian Rodriguez, Laura Lee-Chu, Yixin Fan
# Contact: chloe.thierstein@mail.utoronto.ca 
# Date: March 31, 2024  

# Imports all of the necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Imports the clean and filtered data frame
df = pd.read_csv("filtered_clean_df.csv", low_memory=False)

## Logistic Regression 1: Visible minority status vs. All mental health indicators##

# Encodes the categorical variables
label_encoders = {}
for column in df.select_dtypes(include=['object']).columns:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column])

# Defines the independent variables (aka features) and dependent variable (aka target)
X = df[['Relationship Sat: Relatives or family not living with', 'Relationship Sat: Friends', 'Perceived Mental Health']]
y = df['Visible Minority']

# Splits the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializes and fits a Random Forest classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Creates predictions based on the test set
y_pred = rf_model.predict(X_test)

# Evaluates the accuracy of the model and displays it
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of Logistic Regression 1:", accuracy)

## Logistic Regression 2: Visible minority status vs. Time spent using the internet ##

# Encodes the categorical variables
label_encoders = {}
for column in df.select_dtypes(include=['object']).columns:
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column])

# Defines the independent variables (aka features) and dependent variable (aka target)
X = df[['Time spent using the internet']]
y = df['Visible Minority']

# Splits the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializes and fits a Random Forest classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Creates predictions based on the test set
y_pred = rf_model.predict(X_test)

# Evaluates the accuracy of the model and displays it
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of Logistic Regression 2:", accuracy)