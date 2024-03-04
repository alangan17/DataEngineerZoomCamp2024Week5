if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import os
import pyspark
import requests
from pyspark.sql import SparkSession

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
    url = "https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv"
    # Local filename where to save the downloaded file
    directory = "data"
    filename = "taxi_zone_lookup.csv"
    # Full path to the file
    filepath = os.path.join(directory, filename)

    try:
        download_file(url, directory, filepath)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    spark = (SparkSession.builder
        .master("spark://spark:7077")  # Use Spark master URL
        .appName('test')
        .config("spark.executor.memory", "1g")  # Optional: Adjust memory per executor if needed
        .config("spark.executor.cores", "1")  # Optional: Adjust number of cores per executor if needed
        .getOrCreate()
    )

    df = (spark.read
        .option("header", "true")
        .csv(filepath)
    )

    df.show()

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
