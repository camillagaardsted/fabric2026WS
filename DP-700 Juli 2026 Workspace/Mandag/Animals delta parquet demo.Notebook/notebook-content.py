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

# ## Demo af managed tables og delta format

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
foldername="Files/superusersdata"
filename="animals.csv"
mssparkutils.fs.mkdirs(foldername)
filepath=foldername+"/"+filename
data="Id,Navn\n1,Hest\n2,Kat\n3,Hund"
mssparkutils.fs.put(filepath,data,True)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

mssparkutils.fs.ls(foldername)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

print(mssparkutils.fs.head(filepath))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# File location and type
file_location = "Files/superusersdata/animals.csv"
file_type = "csv"

# CSV options
infer_schema = "true"
first_row_is_header = "true"
delimiter = ","

# The applied options are for CSV files. For other file types, these will be ignored.
df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)

permanent_table_name = "animalsTable"

df.write.format("delta").saveAsTable(permanent_table_name)
# nu gør vi det samme, men med delta formatet
#df.write.format("delta").saveAsTable(permanent_table_name)
# default format er delta nu i den spark version vi kører her
#df.write.saveAsTable(permanent_table_name)



# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# df er vores dataframe

df.write.format("delta").saveAsTable("dbo.myexternaltable",path="Files/myexternaltable2")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM animalsTable


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC INSERT INTO animalsTable
# MAGIC VALUES(4,'Giraf')

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM animalsTable


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC -- not allowed for parquet file for table The feature is not supported: Table 
# MAGIC -- animalstable` does not support DELETE
# MAGIC DELETE FROM animalsTable
# MAGIC WHERE Id=4


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC -- not allowed
# MAGIC --UPDATE TABLE is not supported for parquet file tables temporarily.
# MAGIC UPDATE animalsTable
# MAGIC SET Navn='Flodhest'
# MAGIC WHERE Id=1


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM animalsTable


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


%%sql
-- vi er i spark sql  - det her nogle specielle kommandoer som giver os info om en tabel
DESCRIBE TABLE  animalsTable

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC -- managed  table means files will be removed if we drop the table
# MAGIC -- Type,MANAGED
# MAGIC -- Provider,parquet
# MAGIC DESCRIBE TABLE EXTENDED  animalsTable

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql 
# MAGIC DROP TABLE animalstable


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC -- we can view the history for our delta table
# MAGIC DESCRIBE HISTORY animalstable

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC -- time travel
# MAGIC -- Use Delta Lake time travel syntax: VERSION AS OF <n>
# MAGIC -- Original query failed due to incorrect 'as of version' ordering
# MAGIC SELECT      *
# MAGIC FROM        animalstable VERSION AS OF 1

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

for i in range(1,10):
    spark.sql(f"INSERT INTO animalsTable VALUES({i},'Tiger{i}')")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC DESCRIBE HISTORY animalstable

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC -- vi har optimize som en kommando til at undgå small file problem - det er en spark kommando
# MAGIC OPTIMIZE animalsTable


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC DESCRIBE HISTORY animalstable

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC -- we can do time travel using our delta log -
# MAGIC -- so we want to go back to only the 3 animals
# MAGIC 
# MAGIC SELECT      *
# MAGIC FROM        animalstable VERSION AS OF 3
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT      *
# MAGIC FROM        animalstable VERSION AS OF 67


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql 
# MAGIC -- select to a given timestamp 2025-11-25T14:15:51Z
# MAGIC SELECT      *
# MAGIC FROM        animalstable TIMESTAMP AS OF '2025-11-25 14:15:51.000'


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC -- now we restore to a specific version
# MAGIC 
# MAGIC RESTORE TABLE animalstable VERSION AS OF 3

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# we change the default setting about checking the duration for vacuum

spark.conf.set(
    "spark.databricks.delta.retentionDurationCheck.enabled",
    "false"
)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC VACUUM animalsTable RETAIN 0 HOURS

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC DESCRIBE HISTORY animalstable

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
