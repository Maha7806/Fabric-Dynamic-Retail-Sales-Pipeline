#!/usr/bin/env python
# coding: utf-8

# ## NB_Silver_transformation
# 
# null

# In[ ]:


from pyspark.sql.functions import *

# Read Silver table
df = spark.read.table("silver_sales")

# Add Year, Month, Quarter
gold_df = (
    df
    .withColumn("Year", year(col("OrderDate")))
    .withColumn("Month", month(col("OrderDate")))
    .withColumn("MonthName", date_format(col("OrderDate"), "MMMM"))
    .withColumn("Quarter", quarter(col("OrderDate")))
)

# Write Gold table
gold_df.write.mode("overwrite").saveAsTable("Gold_Sales")

print("Gold_Sales created successfully")

