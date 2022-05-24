# Databricks notebook source
# MAGIC %md
# MAGIC # Project: What Color is Your Car?

# COMMAND ----------

# MAGIC %md
# MAGIC ## Overview
# MAGIC Orange Coast College in Costa Mesa, California would like to test the claim that more than 17% of its students drive a white car. This claim will be tested at a level .05 level of significance (α).

# COMMAND ----------

# MAGIC %md
# MAGIC ## Methodology
# MAGIC ### Given data
# MAGIC We are given the following data:

# COMMAND ----------

displayHTML("<img src='files/sample_data.png'/>")

# COMMAND ----------

import pandas as pd
df = pd.DataFrame(
    {
        "color": ['Black', 'White', 'Silver', 'Blue', 'Gray', 'Red', 'Green', 'Yellow'],
        "count": [10, 15, 13,  4,  6,  2,  1,  1]
    }
)
display(df,showindex=False)

# COMMAND ----------

df.columns

# COMMAND ----------

df.values


# COMMAND ----------

import matplotlib.pyplot as plt

# COMMAND ----------

df.plot.bar()

# COMMAND ----------


