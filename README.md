# Data Engineering Zoomcamp 2024 Week 5
Batch processing using Apache Spark

[Lesson materials](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/05-batch)

## Lesson Learned

```mermaid
mindmap
    id1)Week 5: Batch Processing(

```
### 1. Introduction to Batch Processing
#### 1. Batch vs Streaming
#### 2. Types of Batch Processing
#### 3. Orchestrating batch jobs
#### 4. Advantages and disadvantages of Batch jobs

### 2. Spark Introduction
- What is Apache Spark?
  - Data Processing Engine for batch and streaming jobs
  - Support different languages
    -  Java
    -  Scala
    -  Python
    -  R
- When to use Spark?
  - dataset that you cannot be handled in SQL (e.g. Machine Learning)

### 3. [Installing Spark](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/05-batch/setup/pyspark.md)

### 4. First look at Spark/ PySpark

### 5. Spark DataFrames

### 6. Spark SQL

### 7. Joins in Spark

### 8. RDDs

### 9. Spark Internals

### 10. Spark and Docker

### 11. Running Spark in the Cloud

### 12. Connecting Spark to a DWH

## Homework

In this homework we'll put what we learned about Spark in practice.

For this homework we will be using the FHV 2019-10 data found here. [FHV Data](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-10.csv.gz)

### Question 1: 

**Install Spark and PySpark** 

- Install Spark
- Run PySpark
- Create a local spark session
- Execute spark.version.

What's the output? 3.4.1

> [!NOTE]
> To install PySpark follow this [guide](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/05-batch/setup/pyspark.md)

### Question 2: 

**FHV October 2019**

Read the October 2019 FHV into a Spark Dataframe with a schema as we did in the lessons.

Repartition the Dataframe to 6 partitions and save it to parquet.

What is the average size of the Parquet (ending with .parquet extension) Files that were created (in MB)? Select the answer which most closely matches.

- 1MB
- -> 6MB
- 25MB
- 87MB



### Question 3: 

**Count records** 

How many taxi trips were there on the 15th of October?

Consider only trips that started on the 15th of October.

- 108,164
- 12,856
- 452,470
- -> 62,610

> [!IMPORTANT]
> Be aware of columns order when defining schema

### Question 4: 

**Longest trip for each day** 

What is the length of the longest trip in the dataset in hours?

- -> 631,152.50 Hours
- 243.44 Hours
- 7.68 Hours
- 3.32 Hours



### Question 5: 

**User Interface**

Spark’s User Interface which shows the application's dashboard runs on which local port?

- 80
- 443
- -> 4040
- 8080



### Question 6: 

**Least frequent pickup location zone**

Load the zone lookup data into a temp view in Spark</br>
[Zone Data](https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv)

Using the zone lookup data and the FHV October 2019 data, what is the name of the LEAST frequent pickup location Zone?</br>

- East Chelsea
- -> Jamaica Bay
- Union Sq
- Crown Heights North


### Submitting the solutions

- Form for submitting: https://courses.datatalks.club/de-zoomcamp-2024/homework/hw5
- Deadline: See the website