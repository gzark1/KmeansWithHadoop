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
- Java: The MapReduce programs in this project are written in Java, so you should have Java Development Kit (JDK)
  installed.

## Usage

1. Clone the repository to your local machine:
   git clone https://github.com/maarioos123/KmeansWithHadoop.git


2. Prepare input data:

   The input data for K-means algorithm are generated from the points_generator.py and you can get it by running the
   script or directly

3. Specify the initial centroids in the centroids.txt

4. Upload input data to Hadoop:

   Upload the input data file to Hadoop HDFS using the following command:
   `hadoop fs -put /path/to/input-data /input`

5. Run the K-means algorithm:

    Use the following command to run the K-means algorithm:

    `python main.py -input /input -output /output -jar `

    Where -input is the path to input file, -output is the path to the output file
    and -jar is the path to the hadoop streaming jar.Note that we are using mapper and reducer in python so we have to use
    hadoop python streaming.For example you can use : 

    `python main.py -jar C:\hadoop\share\hadoop\tools\lib\hadoop-st -input /input/input.txt -output /output`

6. Retrieve the results:

    After the MapReduce job completes, you can retrieve the output results from Hadoop HDFS using the following command:
    
    `hadoop fs -get <path_to_final_output_of_algorithm_iteration>`