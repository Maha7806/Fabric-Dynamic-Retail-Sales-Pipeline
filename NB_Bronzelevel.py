#!/usr/bin/env python
# coding: utf-8

# ## NB_Bronzelevel
# 
# null

# In[1]:


from pyspark.sql import dataframe
df = spark.read.option("header","true").csv("Files/Raw_data/*.csv")
display(df.limit(10))


# In[2]:


df.write.mode("Overwrite").saveAsTable("Bronze_Sales")


# In[3]:


df.count()

