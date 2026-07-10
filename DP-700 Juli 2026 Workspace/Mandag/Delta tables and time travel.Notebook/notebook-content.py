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

# # Lab 3 EXTRA Delta tables and time travel
# 
# # Exercise 1
# 
# a) Create a new notebook called "Lab 3 delta tables and time travel" with default language SQL.
# 
# b) Create a schema called deltademo in your catalog
# 
# c) Create the table below in your deltademo schema


# CELL ********************

CREATE TABLE students 
  (id INT, name STRING, value DOUBLE);

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************


# MARKDOWN ********************

# d) Query the table which should of course be empty.
# 
# e) Study what you get with the DESCRIBE TABLE command for  table
# 
# f) Add extended to the DESCRIBE TABLE syntax to see what you get about your table. Notice the table is managed and provider is delta. Also notice where data is stored.
# 
# g) Before you run the statement below. Ask your self how many transactions will you get in the history for the table? Hint each INSERT, UPDATE, DELETE and MERGE statement gives a transaction.
# 
# h) Execute the SQL below

# CELL ********************

INSERT INTO  VALUES (1, "Yve", 1.0);
INSERT INTO  VALUES (2, "Omar", 2.5);
INSERT INTO  VALUES (3, "Elia", 3.3);

INSERT INTO 
VALUES 
  (4, "Ted", 4.7),
  (5, "Tiffany", 5.5),
  (6, "Vini", 6.3);
  
UPDATE  
SET value = value + 1
WHERE name LIKE "T%";

DELETE FROM  
WHERE value > 6;

-- temp view kun synligt i vores session og dør bagefter
CREATE OR REPLACE TEMP VIEW updates(id, name, value, type) AS VALUES
  (2, "Omar", 15.2, "update"),
  (3, "", null, "delete"),
  (7, "Blue", 7.7, "insert"),
  (11, "Diya", 8.8, "update");
  
MERGE INTO  b
USING updates u
ON b.id=u.id
WHEN MATCHED AND u.type = "update"
  THEN UPDATE SET *
WHEN MATCHED AND u.type = "delete"
  THEN DELETE
WHEN NOT MATCHED AND u.type = "insert"
  THEN INSERT *;


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# 
# # Exercise 2 Time travel
# 1. Use time travel to query the `students` table as it was before the merge operation using the version number. What were the records in the table at that time?
# 2. Use time travel to query the `students` table as it was after the first 4 INSERT statements but before the UPDATE and DELETE statements. What were the records in the table at that time?
# 3. Use time travel to restore the `students` table to version 4.
# 4. Query the `students` table after restoring it to version 4. What are the records in the table now?
# 5. Study the history for the table and notice that the RESTORE operation also creates a version. What is the version number for the RESTORE operation?

# CELL ********************

from notebookutils import mssparkutils
from pyspark.sql.types import *
from pyspark.sql.functions import *

# Create a folder
inputPath = 'Files/data/'
mssparkutils.fs.mkdirs(inputPath)

# Create a stream that reads data from the folder, using a JSON schema
jsonSchema = StructType([
StructField("device", StringType(), False),
StructField("status", StringType(), False)
])
iotstream = spark.readStream.schema(jsonSchema).option("maxFilesPerTrigger", 1).json(inputPath)

# Write some event data to the folder
device_data = '''{"device":"Dev1","status":"ok"}
{"device":"Dev1","status":"ok"}
{"device":"Dev1","status":"ok"}
{"device":"Dev2","status":"error"}
{"device":"Dev1","status":"ok"}
{"device":"Dev1","status":"error"}
{"device":"Dev2","status":"ok"}
{"device":"Dev2","status":"error"}
{"device":"Dev1","status":"ok"}'''

mssparkutils.fs.put(inputPath + "data.txt", device_data, True)

print("Source stream created...")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Write the stream to a delta table
delta_stream_table_path = 'Tables/dbo/iotdevicedata'
checkpointpath = 'Files/delta/checkpoint'
deltastream = iotstream.writeStream.format("delta").option("checkpointLocation", checkpointpath).start(delta_stream_table_path)
print("Streaming to delta sink...")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM dbo.IotDeviceData;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Add more data to the source stream
more_data = '''{"device":"Dev1","status":"ok"}
{"device":"Dev1","status":"ok"}
{"device":"Dev1","status":"ok"}
{"device":"Dev1","status":"ok"}
{"device":"Dev1","status":"error"}
{"device":"Dev2","status":"error"}
{"device":"Dev1","status":"ok"}'''

mssparkutils.fs.put(inputPath + "more-data.txt", more_data, True)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM dbo.IotDeviceData;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark.streams.active

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

deltastream.status

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

deltastream.stop()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
