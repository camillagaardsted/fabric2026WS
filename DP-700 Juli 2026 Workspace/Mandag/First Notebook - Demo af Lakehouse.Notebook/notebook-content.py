# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "cc799b82-40e1-4494-9e90-941d4f52e430",
# META       "default_lakehouse_name": "MandagLakehouse",
# META       "default_lakehouse_workspace_id": "0b6a0599-c257-4d45-b1a0-752287cd3941",
# META       "known_lakehouses": [
# META         {
# META           "id": "cc799b82-40e1-4494-9e90-941d4f52e430"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# # Vores første notebook - en demo af Lakehouse og en notebook
# 
# ## Demo
# 
# Her er vores første notebook. En notebook består af celler med kode og kan have tekst forklaringer i markdownceller.


# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
print('Godformiddag til Python inde i vores notebook - og til Spark!')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# nu indlæser jeg vores data fra en af csv filerne
# pga tegnestiften ved Spark  den skal kigge under mandagsLakehouse
# vi indlæser altid til en Spark DataFrame- for at få fuld gevinst af Spark
filename='Files/raspberrydata/data2021_01_25_08_47_02.csv'
df = spark.read.csv(filename)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# nu indlæser jeg vores data fra en af csv filerne
# pga tegnestiften ved Spark  den skal kigge under mandagsLakehouse
# vi indlæser altid til en Spark DataFrame- for at få fuld gevinst af Spark
filename='Files/raspberrydata/data2021_01_25_08_47_02.csv'
df = spark.read.csv(filename,header=True, inferSchema=True)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.printSchema()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# nu indlæser jeg vores data fra en af csv filerne
# pga tegnestiften ved Spark  den skal kigge under mandagsLakehouse
# vi indlæser altid til en Spark DataFrame- for at få fuld gevinst af Spark
filename_with_wildcard='Files/raspberrydata/data*.csv'
df = spark.read.csv(filename_with_wildcard,header=True, inferSchema=True)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

filename_with_wildcard='Files/raspberrydata/data*.csv'
df = spark.read.csv(filename_with_wildcard,header=True, inferSchema=True)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC -- Det betyder vi nu skifter sprog og kan skrive SQL
# MAGIC CREATE SCHEMA raspberry;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# kommentarer i python
df.write.saveAsTable('raspberry.sensordata')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT      *
# MAGIC FROM        raspberry.sensordata

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# kommentarer i python - hvor havner denne tabel ?
df.write.saveAsTable('sensordata_1')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql 
# MAGIC -- hvad er det for noget sql vi kan skrive her?
# MAGIC -- Det er Spark SQL vi har her i vores notebook
# MAGIC 
# MAGIC -- det er spark SQL -- 3.5.5 e097fc73ee470afb0a4253aae126bb32fad2fe7c
# MAGIC SELECT version()

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC -- her er det lidt forvirrende at vi ikke ser schema korrekt - 
# MAGIC SELECT  current_schema()
# MAGIC         

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC -- det her går ikke -d et er IKKE t-sql - det er spark sql her i den her celle
# MAGIC SELECT @@version

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

path='Files/vm/worldcup.squads.json'
df=spark.read.json(path,multiLine=True)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df=df.withColumnRenamed('name','Country')
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import pyspark.sql.functions as F
df=df.select('Country',F.explode('players').alias('player'))
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df=df.select('Country','player.*')
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
