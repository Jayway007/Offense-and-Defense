# [Hadoop](https://hadoop.apache.org/)
The Apache Hadoop software library is a framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models.

Its core components are HDFS and MapReduce, which provide storage and calculation frame work for wide-range data.

## [HDFS](https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html)
The Hadoop Distributed File System (HDFS) is a distributed file system designed to run on commodity hardware. It has many similarities with existing distributed file systems.

## [MapReduce](https://research.google/pubs/pub62/)
MapReduce is a programming model and an associated implementation for processing and generating large data sets. Users specify a map function that processes a key/value pair to generate a set of intermediate key/value pairs, and a reduce function that merges all intermediate values associated with the same intermediate key. 


# [Hive](https://hive.apache.org/)
Hive is a data warehouse analysis system, providing SQL search to analyze data stored in HDFS. It can reflect structured data into a database table and translate SQL into MapReduce task to run.

# [Spark](https://spark.apache.org/)
Apache Spark is a multi-language engine for executing data engineering, data science, and machine learning on single-node machines or clusters, including Python, SQL, Scala, Java and R.

## [PySpark](https://spark.apache.org/docs/latest/api/python/)
PySpark is an interface for Apache Spark in Python. PySpark supports most of Spark’s features such as Spark SQL, DataFrame, Streaming, MLlib (Machine Learning) and Spark Core

### Spark Core
Spark Core is the underlying general execution engine for the Spark platform that all other functionality is built on top of. It provides an RDD (Resilient Distributed Dataset) and in-memory computing capabilities.

# [Flink](https://flink.apache.org/)
Apache Flink is a framework and distributed processing engine for stateful computations over unbounded and bounded data streams. Flink has been designed to run in all common cluster environments, perform computations at in-memory speed and at any scale.
