# models/model.py

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load sample data
data = pd.read_csv('data/sample_data.csv')

# Select relevant features
features = data[['height', 'weight', 'chest', 'waist', 'hip']]

# Standardize the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(features_scaled)

# Add the cluster labels to the original data
data['cluster'] = clusters

# Save the clustered data
data.to_csv('data/clustered_data.csv', index=False)
