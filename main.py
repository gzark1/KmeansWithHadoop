import subprocess
import numpy as np

# Maximum number of iterations
max_iterations = 10  # Update with the desired maximum number of iterations

# Threshold for convergence
convergence_threshold = 0.1  # Update with your desired convergence threshold

# Read initial centroids from centroids.txt file
with open('centroids.txt', 'r') as f:
    initial_centroids = [np.array(list(map(float, line.strip().split(',')))) for line in f]

# Initialize centroids
current_centroids = initial_centroids
# Loop for running k-means iteratively
for i in range(max_iterations):
    print("Running iteration: ", i+1)

    # Hadoop command to run with current centroids as input
    hadoop_cmd = 'hadoop jar C:\\hadoop\\share\\hadoop\\tools\\lib\\hadoop-streaming-3.2.4.jar -input /input/points.txt -output /output/iterations'+str(i)+ \
                 ' -mapper "python mapper.py -centroids {}" -reducer "python reducer.py" '
    # Run the CMD command and capture the output
    output = subprocess.check_output(hadoop_cmd, shell=True)

    # Decode the output from bytes to string
    output = output.decode('utf-8')

    # Print the output
    print(output)

    # Read the final centroids from the output
    # You can implement the logic to parse the centroids from the output here
    with open('centroids.txt', 'r') as f:
        current_centroids = [np.array(list(map(float, line.strip().split(',')))) for line in f]

    # Compare the final centroids with the current centroids for convergence
    converged = True
    for j in range(len(current_centroids)):
        if np.linalg.norm(current_centroids[j] - current_centroids[j]) > convergence_threshold:
            converged = False
            break  # Break out of the loop if any centroid has not converged

    if converged:
        print("Converged! Centroids remain unchanged.")
        break  # Break out of the loop if centroids remain unchanged
    else:
        initial_centroids = current_centroids  # Update current centroids for the next iteration
