if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql import functions as F

@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    
    spark = (SparkSession.builder
        .master("spark://spark:7077")  # Use Spark master URL
        .appName('test')
        .config("spark.executor.memory", "1g")  # Optional: Adjust memory per executor if needed
        .config("spark.executor.cores", "1")  # Optional: Adjust number of cores per executor if needed
        .getOrCreate()
    )
    sc = spark.sparkContext

    # Get the UI web URL
    uiWebUrl = sc.uiWebUrl
    print(uiWebUrl)

    df = spark.read.parquet(data.get("parquet_out_path"))
    df.printSchema()

    df2 = (spark.read
        .option("header", "true")
        .csv("data/taxi_zone_lookup.csv")
    )
    df2.printSchema()

    # Question 6
    df = df.withColumn("trip_duration_hours", (col("dropOff_datetime").cast("long") - col("pickup_datetime").cast("long")) / 3600)
    df2 = df2.withColumn("LocationID", (col("LocationID").cast("int")))

    df.registerTempTable('fhv_data')
    df2.registerTempTable('lookup_data')

    print("Answer 6:")
    spark.sql("""
        SELECT
            lookup_Data.Zone,
            count(*) as cnt
        FROM fhv_data
        LEFT JOIN lookup_data ON 1=1
            AND fhv_data.PUlocationID = lookup_Data.LocationID
        WHERE 1=1
            AND year(fhv_data.pickup_datetime) = 2019
            AND month(fhv_data.pickup_datetime) = 10
        GROUP BY lookup_Data.Zone
        ORDER BY count(*)
    """).show()

    return {
        "parquet_out_path": data.get("parquet_out_path")
    }


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
