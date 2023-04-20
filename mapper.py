import sys
import numpy as np

class KmeansWithHadoop:
    #10 20 30 30 25 15 

    def __init__(self) -> None:
        self.centroids = None
    
    def mapper(self):
        centroid_lines = None
        with open('centroids.txt') as f:
            centroid_lines = f.readlines()
        
        self.centroids = [np.array(line.strip().split(","), dtype=float) for line in centroid_lines]
    
        for line in sys.stdin:
            
            x, y = line.strip().split(",")
            point = np.array((float(x), float(y)))
            distances = [np.linalg.norm(point - c) for c in self.centroids]
            closest_idx = np.argmin(distances)
            centroid = self.centroids[closest_idx]
            print("{0},{1}\t{2},{3}".format(centroid[0], centroid[1], x, y))

    def main(self):

        self.mapper()
        sys.stdin = sys.__stdin__
    
test = KmeansWithHadoop()
test.main()