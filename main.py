import subprocess

# Hadoop command to run
hadoop_cmd = 'hadoop jar C:\\hadoop\\share\\hadoop\\tools\\lib\\hadoop-streaming-3.2.4.jar -input /input/points.txt -output /output/new22 -mapper "python mapper.py" -reducer "python reducer.py" '

# CMD command to run

# Run the CMD command and capture the output
output = subprocess.check_output(hadoop_cmd, shell=True)

# Decode the output from bytes to string
output = output.decode('utf-8')

# Print the output
print(output)
hadoop_cmd = 'hadoop jar C:\\hadoop\\share\\hadoop\\tools\\lib\\hadoop-streaming-3.2.4.jar -input /input/points.txt -output /output/new23 -mapper "python mapper.py" -reducer "python reducer.py" '
output = subprocess.check_output(hadoop_cmd, shell=True)

# Decode the output from bytes to string
output = output.decode('utf-8')

# Print the output
print(output)