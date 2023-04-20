import subprocess
import numpy as np

# Maximum number of iterations
max_iterations = 10  # Update with the desired maximum number of iterations

# Threshold for convergence
convergence_threshold = 0.01  # Update with your desired convergence threshold

# Read initial centroids from centroids.txt file
with open('centroids.txt') as f:
    centroid_lines = f.readlines()
        
initial_centroids = [np.array(line.strip().split(","), dtype=float) for line in centroid_lines]

# Initialize centroids
current_centroids = initial_centroids
# Loop for running k-means iteratively
for i in range(max_iterations):
    print("Running iteration: ", i+1,"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    if i==0:
        with open("centroids.txt", "w") as f:
            f.write("10,20\n30,30\n25,15")

    # Hadoop command to run with current centroids as input
    hadoop_cmd = 'hadoop jar C:\\hadoop\\share\\hadoop\\tools\\lib\\hadoop-streaming-3.2.4.jar -input /input/points.txt -output /output/iterations12'+str(i)+ \
                 ' -mapper "python mapper.py" -reducer "python reducer.py" '
    # Run the CMD command and capture the output
    output = subprocess.check_output(hadoop_cmd, shell=True)

    # Decode the output from bytes to string
    output = output.decode('utf-8')

    # Print the output
    print(output)

    # Read the final centroids from the output
    # You can implement the logic to parse the centroids from the output here
    with open('centroids.txt') as f:
        centroid_lines = f.readlines()
            
    current_centroids = [np.array(line.strip().split(","), dtype=float) for line in centroid_lines]

    # Compare the final centroids with the current centroids for convergence
    converged = True
    for j in range(len(current_centroids)): 
        print(initial_centroids[j], current_centroids[j])
        if np.linalg.norm(initial_centroids[j] - current_centroids[j]) > convergence_threshold:
            converged = False
            break  # Break out of the loop if any centroid has not converged

    if converged:
        print("Converged! Centroids remain unchanged.")
        break  # Break out of the loop if centroids remain unchanged
    else:
        initial_centroids = current_centroids  # Update current centroids for the next iteration
