#!/usr/bin/env python
# coding: utf-8

# ## NB_GoldLayerTransformation
# 
# null

# In[4]:


from pyspark.sql.functions import *

df = spark.read.table("Gold_Sales")
gold_summary = (
    df.groupBy("City", "Category")
      .agg(
          sum("Quantity").alias("TotalQuantity"),
          count("OrderID").alias("TotalOrders")
      )
)
gold_summary.write.mode("overwrite").saveAsTable("Gold_SalesSummary")

display(gold_summary)

