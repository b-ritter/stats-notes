# Databricks notebook source
import seaborn as sns
sns.set(style="whitegrid")

# COMMAND ----------

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

displayHTML("""<img width="600px" src='files/shared_uploads/britter6@student.cccd.edu/Screen_Shot_2022_05_24_at_10_52_24_AM.png'/>""")

# COMMAND ----------

# MAGIC %md
# MAGIC This data must be digitized, cleaned and formatted for analysis. The table below follows the conventions for [tidy data](https://r4ds.had.co.nz/tidy-data.html#fig:tidy-structure), where variables constitute columns and observations form rows.

# COMMAND ----------

import pandas as pd
df = pd.DataFrame(
    {
        "Color of car": ['Black', 'White', 'Silver', 'Blue', 'Gray', 'Red', 'Green', 'Yellow'],
        "Number of cars": [10, 15, 13,  4,  6,  2,  1,  1]
    }
)

# COMMAND ----------

display(df,showindex=False)

# COMMAND ----------

plt.figure(figsize=(10,5))
plt.title("Count of cars by color in OCC Parking Lots")
car_bars = sns.barplot(x="Color of car", y="Number of cars", data=df)
f = car_bars.get_figure()
f.savefig("/dbfs/FileStore/car_plot.svg")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Sampling Techniques
# MAGIC 
# MAGIC While this data is given to us, in the real world the data should be randomly sampled — a Simple Random Sample or SRS. A simple method of obtaining this data could be to conduct surverys at the four major parking lots in OCC on a particular day of week and time range. These lots are the Adams Lot, Lot G, Lot C and Lot E. Keeping the day and time constant will help to avoid lurking variables. Since the lots are large, 8 student researchers should be sufficeint to conduct this survey simultaneously. Each researcher should aim for about 25 — 50 responses.
# MAGIC 
# MAGIC Another option, shown below, could be a type of web survey. In this case, a key concern would be to obtain a sufficient number of responses. If the researcher were to obtain the list of email addresses for all approximately [22,000 OCC students](https://prod.orangecoastcollege.edu/about/), they could offer a chance to win a prize of say $25 to increase participation. As long as the sample size is under about 1000, or 5% of the total enrollment, this will work for our study. (See below)

# COMMAND ----------

displayHTML("""
<form>
<label for="cars">What color is your car? Please choose one.</label>
<p>
<input type="radio" name="carcolor">Black</input>
<input type="radio" name="carcolor">White</input>
<input type="radio" name="carcolor">Silver</input>
<input type="radio" name="carcolor">Blue</input>
<input type="radio" name="carcolor">Gray</input>
<input type="radio" name="carcolor">Red</input>
<input type="radio" name="carcolor">Green</input>
<input type="radio" name="carcolor">Yellow</input>
</p>
<button type="button">Submit</button>
</form>
""")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Statistical Analysis

# COMMAND ----------

# MAGIC %md 
# MAGIC For this dataset we will use the Z distribution to test the following claim: 
# MAGIC $$ H_0: \text{The proportion of white cars at OCC} = .17 $$
# MAGIC $$ H_1: \text{The proportion of white cars at OCC} > .17 $$

# COMMAND ----------

# MAGIC %md
# MAGIC To conduct a one proportion Z test, we need to meet three requirements. 
# MAGIC 1. Data is SRS
# MAGIC 1. \\(np_0(1-p_0) >= 10\\)
# MAGIC 1. \\(n<=.05N \\)

# COMMAND ----------

# MAGIC %md
# MAGIC The first requirement is given in the project description. For the second and third requirements, we need to know the total number of cars sampled \\(n\\).

# COMMAND ----------

df['Number of cars'].sum()

# COMMAND ----------

# MAGIC %md
# MAGIC Therefore, \\(n = 52\\).

# COMMAND ----------

# MAGIC %md
# MAGIC For our second requirement, \\(p_0 = .17\\). 
# MAGIC 
# MAGIC Since \\(52 \times .17 \times (1-.17)) = < 10\\) our second requirement is _not_ satisfied.

# COMMAND ----------

# MAGIC %md
# MAGIC Since \\(N\\) (our population size) is approximately 22k, our sample size should be no more than \\(22000 \times  .05 = 1100\\). In our case \\(n < .05N\\) so our third requirement is satisfied. Because the second requirement, failed, we can not use a one parameter Z test and must use the binomial distribution instead. In the actual study, this requirement could be met by increasing the sample size.

# COMMAND ----------

# MAGIC %md
# MAGIC # Approcah
# MAGIC In this paper, we will compare two computational packages, [statsmodels](https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.binom_test.html#statsmodels.stats.proportion.binom_test) and the TI-84 1-binomcdf to compute the P-value of obtaining a sample of size 52 with greater than .17 white cars.

# COMMAND ----------

from statsmodels.stats.proportion import binom_test

# COMMAND ----------

p_value = 1 - binom_test(15, 52, .17, alternative='smaller')

# COMMAND ----------

# MAGIC %md
# MAGIC # Conclusion

# COMMAND ----------

# MAGIC %md
# MAGIC Because p < .05, there is sufficient evidence to reject the null hypothesis and support the claim that the proportion of white cars at OCC is greater than .17. Some factors for this might be due to the warm climate in Southern California. A white car might be cooler than a dark one. White cars also tend to show less dirt which also make them a popular choice.

# COMMAND ----------



# COMMAND ----------

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

min_z, max_z = -4, 4
x_axis = np.arange(min_z, max_z, 0.001)

critical_region_cutoff = norm.ppf(.95)
critical_region = np.arange(critical_region_cutoff, max_z, .001)

test_statistic = norm.ppf(1 - p_value)
p_value = np.arange(test_statistic, max_z, .001)

plt.figure(figsize=(15,5))
plt.fill_between(critical_region, norm.pdf(critical_region), color="lightgray")
plt.fill_between(p_value, norm.pdf(p_value), color="darkgray")
plt.plot(x_axis, norm.pdf(x_axis, 0, 1))
plt.annotate(
    "Test Statistic", (test_statistic,0), 
    (3,.15), 
    arrowprops={"arrowstyle": "->", "color": "black"}
)
plt.annotate(
    "Zα", 
    (critical_region_cutoff,0), 
    (1,.15), 
    arrowprops={"arrowstyle": "->", "color": "black"}
)
f = plt.gcf()
f.savefig("/dbfs/FileStore/Z_distribution.svg")
plt.show()

# COMMAND ----------


