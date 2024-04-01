# Purpose: The purpose of this code is to perform cluster analysis for our INF412 final project.
# Authors: Chloe Thierstein, Sebastian Rodriguez, Laura Lee-Chu, Yixin Fan
# Contact: chloe.thierstein@mail.utoronto.ca 
# Date: March 31, 2024 

# Imports all of the necessary libraries
import pandas as pd
import mord as m
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Imports the data clean and filtered numeric data frame
df = pd.read_csv("filtered_clean_numeric_df.csv", low_memory=False)

# Initializes the StandardScaler object to standardize our features
scaler = StandardScaler()

# Standardizes the data
df_scaled = scaler.fit_transform(df)

# Performs KMeans clustering by setting the number to 3 and to the random state for better reproducibility 
kmeans = KMeans(n_clusters=3, random_state=0).fit(df_scaled)

# Gets the cluster labels and centers
cluster_labels = kmeans.labels_ 
cluster_centers = kmeans.cluster_centers_

# Displays the cluster centers
print("Cluster Centers:")
print(cluster_centers)