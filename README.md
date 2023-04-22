# Kmeans with MapReduce

## Description

This project implements a K-means clustering algorithm using Hadoop MapReduce. K-means is a popular unsupervised machine
learning algorithm used for clustering data into groups based on similarity. This implementation is designed to work
with large-scale data sets that can be processed in parallel using Hadoop.We have a Windows PC setup with Apache Hadoop installed,
and we utilize Hadoop Streaming to execute Python scripts as the mapper and reducer for our MapReduce jobs.

## Prerequisites

Before running this project, make sure you have the following software installed:

- Hadoop: This implementation relies on Hadoop for distributed processing. You should have a working Hadoop cluster set
  up and configured.
- Java:  In order to run Hadoop, regardless of the language used to write the MapReduce programs, you still need to have the Java Development Kit (JDK) installed on your machine. This is because Hadoop itself is written in Java and requires the JDK to run.

## Usage

1. Clone the repository to your local machine:
   git clone https://github.com/maarioos123/KmeansWithHadoop.git


2. Prepare input data:

   The input data for K-means algorithm are generated from the points_generator.py and you can get it by running the
   script or directly

3. Specify the initial centroids in the centroids.txt

4. Ensure that your Hadoop server is running. To start the server, navigate to the hadoop/sbin directory in your Hadoop installation directory. For Windows, run the `start-all.cmd` script. For Linux, run the `start-all.sh` script.

5. Upload input data to Hadoop:

   Upload the input data file to Hadoop HDFS using the following command:
   `hadoop fs -put /path/to/input-data /input`

6. Run the K-means algorithm:

    Use the following command to run the K-means algorithm:

    `python main.py -input /input -output /output -jar path_to_hadoop_streaming`

    Where -input is the path to input file, -output is the path to the output file
    and -jar is the path to the hadoop streaming jar.Note that we are using mapper and reducer in python so we have to use
    hadoop python streaming.For example you can use : 

    `python main.py -jar C:\hadoop\share\hadoop\tools\lib\hadoop-st -input /input/input.txt -output /output`

7. Retrieve the results:

    After the MapReduce job completes, you can retrieve the output results from Hadoop HDFS using the following command:
    
    `hadoop fs -get <path_to_final_output_of_algorithm_iteration>`
8. To verify the results, execute the "test_kmeans.py" script and review its output. This script employs scikit-learn to solve the same problem and allows for a comparison of the resulting clusters. 
