from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.session import SparkSession
from pyspark.sql.dataframe import DataFrame
from pyspark.sql import Row
from pyspark import SQLContext
from pyspark.sql.functions import  explode
import pyspark.sql.functions as F
spark = SparkSession.builder.master("local[*]").appName("JSON").getOrCreate()
sqlContext = SQLContext(sparkContext=spark.sparkContext, sparkSession=spark)
df = spark.read.option("multiline","true").json(r'C:\Users\rachowdary\Downloads\source.json')
df1 = df.select(explode("persons").alias("persons"))
df2 = df1.select(
   F.col("persons.name").alias("persons_name")
 , F.col("persons.age").alias("persons_age")
 , explode("persons.cars").alias("persons_cars_brands")
 , F.col("persons_cars_brands.name").alias("persons_cars_brand")
)

df3 = df2.select(
   F.col("persons_name")
 , F.col("persons_age")
 , F.col("persons_cars_brand")
 , explode("persons_cars_brands.models").alias("persons_cars_model")
)


df3.write.csv('jsonData.csv')
