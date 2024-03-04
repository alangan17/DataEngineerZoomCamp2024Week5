if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import os
import pyspark
import requests
from pyspark.sql import SparkSession
from pyspark.sql import types

import requests

def download_file(url, directory, filepath):
    # Check if the directory exists, create it if it doesn't
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    
    # Send a GET request to the URL
    response = requests.get(url)
    # Raise an exception if the request was unsuccessful
    response.raise_for_status()

    # Open the local file for writing in binary mode
    with open(filepath, "wb") as f:
        # Write the content of the response to the file
        f.write(response.content)
    print(f"File '{filepath}' has been downloaded successfully.")

@data_loader
def load_data(**kwargs):
    """
    Template code for loading data from any source.

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # URL of the file to be downloaded
    url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/fhv_tripdata_2019-10.csv.gz"
    # Local filename where to save the downloaded file
    directory = "data/fhv_201910"
    filename = "fhv_tripdata_2019-10.csv.gz"
    # Full path to the file
    filepath = os.path.join(directory, filename)

    # try:
    #     download_file(url, directory, filepath)
    # except requests.exceptions.RequestException as e:
    #     print(f"An error occurred: {e}")

    spark = (SparkSession.builder
        .master("spark://spark:7077")  # Use Spark master URL
        .appName('test')
        .config("spark.executor.memory", "1g")  # Optional: Adjust memory per executor if needed
        .config("spark.executor.cores", "1")  # Optional: Adjust number of cores per executor if needed
        .getOrCreate()
    )
    print(f"{spark.version=}")

    schema = types.StructType([
        types.StructField('dispatching_base_num', types.StringType(), True),
        types.StructField('pickup_datetime',types.TimestampType(), True),
        types.StructField('dropOff_datetime', types.TimestampType(), True),
        types.StructField('PUlocationID', types.IntegerType(), True),
        types.StructField('DOlocationID', types.IntegerType(), True),
        types.StructField('SR_Flag', types.StringType(), True),
        types.StructField('Affiliated_base_number', types.StringType(), True)
    ])

    df = (spark.read
        .option("header", "true")
        .schema(schema)
        .csv(filepath)
    )

    print(f"{df.schema=}")

    df = df.repartition(6)
    parquet_out_path = 'data/fhv_201910_repartition'
    (df.write
        .format('parquet')
        .mode('overwrite')
        .save(parquet_out_path)
    )

    return {
        "parquet_out_path": parquet_out_path
    }


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
