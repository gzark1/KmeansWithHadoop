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
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Run Hadoop Streaming job with input and output file paths')

# Add arguments for input file path, output file path, and Hadoop Streaming JAR path
parser.add_argument('-input', required=True, type=str, help='Input file path')
parser.add_argument('-output', required=True,type=str, help='Output file path')
parser.add_argument('-jar', required=True,type=str, help='Path to Hadoop Streaming JAR')

# Parse the command line arguments
args = parser.parse_args()

# Extract the input file path, output file path, and Hadoop Streaming JAR path from the command line arguments
input_path = args.input
output_path = args.output
jar_path = args.jar

# Build the Hadoop command with the input and output file paths, and the Hadoop Streaming JAR path


# Initialize centroids
current_centroids = initial_centroids
# Loop for running k-means iteratively
for i in range(max_iterations):
    print("Running iteration: ", i + 1, "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    if i == 0:
        with open("centroids.txt", "w") as f:
            f.write("10,20\n30,30\n25,15")

    # Hadoop command to run with current centroids as input
    hadoop_cmd = f'hadoop jar {jar_path} -input {input_path} -output {output_path}' + str(i) + ' -mapper "python ' \
                                                                                               'mapper.py" -reducer ' \
                                                                                               '"python reducer.py"'
    print(hadoop_cmd)
    # # Run the CMD command and capture the output
    # output = subprocess.check_output(hadoop_cmd, shell=True)
    #
    # # Decode the output from bytes to string
    # output = output.decode('utf-8')
    #
    # # Print the output
    # print(output)
    #
    # # Read the final centroids from the output
    # # You can implement the logic to parse the centroids from the output here
    # with open('centroids.txt') as f:
    #     centroid_lines = f.readlines()
    #
    # current_centroids = [np.array(line.strip().split(","), dtype=float) for line in centroid_lines]
    #
    # # Compare the final centroids with the current centroids for convergence
    # converged = True
    # for j in range(len(current_centroids)):
    #     print(initial_centroids[j], current_centroids[j])
    #     if np.linalg.norm(initial_centroids[j] - current_centroids[j]) > convergence_threshold:
    #         converged = False
    #         break  # Break out of the loop if any centroid has not converged
    #
    # if converged:
    #     print("Converged! Centroids remain unchanged.")
    #     break  # Break out of the loop if centroids remain unchanged
    # else:
    #     initial_centroids = current_centroids  # Update current centroids for the next iteration
