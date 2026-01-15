# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "6ce79b53-1d54-47e8-b62e-ad13eed78647",
# META       "default_lakehouse_name": "Bronze_WWI",
# META       "default_lakehouse_workspace_id": "9850caab-4873-4485-8b5a-5d9767ab4c73",
# META       "known_lakehouses": [
# META         {
# META           "id": "6ce79b53-1d54-47e8-b62e-ad13eed78647"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC CREATE TABLE IF NOT EXISTS demo_table ( id int ) USING DELTA;
# MAGIC 


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC SHOW TABLES;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
