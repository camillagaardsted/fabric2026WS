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

# ## På jagt efter Messi

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
filename='Files/vm/worldcup.squads.json'
df=spark.read.json(filename,multiLine=True)
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# omdøb kolonne
df = df.withColumnRenamed('name','Country')
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# vi anvender explode funktionen nu til at folde data ud

import pyspark.sql.functions as F
df = df.select('Country',F.explode('players').alias('player'))
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

# CELL ********************

display(df.where("name LIKE '%Messi'"))


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
