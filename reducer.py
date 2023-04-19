#Reduce function should compute the new center for each constructed
#list. All distances are Euclidean
import sys
import numpy
   
def reducer():
    centroids = {}  # dictionary to store centroid coordinates and associated data points

    for line in sys.stdin:
        cx, cy, x, y = line.strip().split(",")
        centroid = (float(cx), float(cy))

        if centroid not in centroids:
            centroids[centroid] = {'points': [], 'count': 0}

        centroids[centroid]['points'].append((float(x), float(y)))
        centroids[centroid]['count'] += 1

    #3 iterations, typwnei ta 3 kainourgia centroids kai ksana trexei o mapper 
    for centroid, data in centroids.items():
        points = data['points']
        count = data['count']

        if count == 0:
            # if no data points assigned to this centroid, keep the previous centroid
            new_centroid = centroid
        else:
            # calculate the mean of all the data points assigned to this centroid
            x_sum = sum([p[0] for p in points])
            y_sum = sum([p[1] for p in points])
            x_mean = x_sum / count
            y_mean = y_sum / count
            new_centroid = (x_mean, y_mean)

        # output the new centroid
        print(f'{new_centroid[0]},{new_centroid[1]}')
