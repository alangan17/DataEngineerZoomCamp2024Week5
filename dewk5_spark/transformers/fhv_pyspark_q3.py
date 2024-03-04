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
    df = spark.read.parquet(data.get("parquet_out_path"))
    df.printSchema()

    # Question 3
    # Convert to date only col
    df=(df
        .withColumn('pickup_datetime', F.to_date(df.pickup_datetime))
        .withColumn('dropOff_datetime', F.to_date(df.dropOff_datetime))
    )

    # Filter dates
    df_filtered = df.filter(
        (col("pickup_datetime") >= "2019-10-15") & 
        (col("pickup_datetime") < "2019-10-16")
    )
    print(f"Answer 3: {df_filtered.count()}")

    return {
        "parquet_out_path": data.get("parquet_out_path")
    }


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
