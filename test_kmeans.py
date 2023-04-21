import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load data from file
data = np.loadtxt('points.txt', delimiter=',')  # assuming the file is in CSV format with comma-separated values
initial_centroids = np.array([[10, 20], [30, 30], [25, 15]])
# Run K-means algorithm with 3 clusters
kmeans = KMeans(n_clusters=3, init=initial_centroids, n_init=10)
kmeans.fit(data)

# Get cluster assignments for each data point
cluster_assignments = kmeans.labels_

# Get cluster centroids
cluster_centroids = kmeans.cluster_centers_

# Print cluster assignments
print("Cluster assignments:")
print(cluster_assignments)

# Print cluster centroids
print("Cluster centroids:")
print(cluster_centroids)

plt.scatter(data[:, 0], data[:, 1], c='black', label='Data Points')
plt.scatter(initial_centroids[:, 0], initial_centroids[:, 1], marker='o', color='blue', s=200, label='Initial Centroids', edgecolors='black', linewidths=2)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-means Clustering')
plt.legend(loc='upper left')  # specify the desired location for the legend
plt.show()
# Plot the cluster assignments and cluster centroids from K-means
plt.scatter(data[:, 0], data[:, 1], c=cluster_assignments, cmap='viridis')
plt.scatter(cluster_centroids[:, 0], cluster_centroids[:, 1], marker='x', color='red', s=200, label='Cluster Centroids')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-means Clustering')
plt.legend(loc='upper left')  # specify the desired location for the legend
plt.show()