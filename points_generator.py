from matplotlib import pyplot as plt
import random
import numpy as np
from scipy.stats import skewnorm

centroids = [(10,20), (30,30), (25,15)]

random.seed(1)
def get_random_distance_from_centroid():
    # Set the skewness parameter
    a = -2

    # Generate a random number using skew-normal distribution
    distance_from_centroid = skewnorm.rvs(a, size=1)

    # Ensure the number is greater than zero
    while distance_from_centroid <= 0:
        distance_from_centroid = skewnorm.rvs(a, size=1)
    

    distance_from_centroid *= 19

    #randomly make the distance positive or negative
    if random.randint(0,1) == 1:
        distance_from_centroid *= -1
    
    return distance_from_centroid  

#erase contents of points.txt file
with open("points.txt", "w") as f:
    pass

#append the points to points.txt
with open("points.txt", "a") as f:
    iterations = 1000000
    for i in range(iterations):
        
        centroid = random.choice(centroids)
        centroid_x = centroid[0]
        centroid_y = centroid[1]
        x_dist_from_centroid = get_random_distance_from_centroid()
        y_dist_from_centroid = get_random_distance_from_centroid()

        x = centroid[0] + x_dist_from_centroid
        
        y = centroid[1] + y_dist_from_centroid
        
        #plt.scatter(x[0], y[0], c="blue", marker =".")
        f.write(f"{x[0]},{y[0]} \n")

plt.show()      