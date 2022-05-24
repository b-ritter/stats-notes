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

display(df,showindex=False)

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
# MAGIC 1. \\(np(1-p) >= 10\\)
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
# MAGIC For our second requirement, \\(p_0 = \frac{15}{52}=0.2884615385\\). 
# MAGIC 
# MAGIC Since \\(0.2884615385 * (1 - 0.2884615385) = 0.2052514793) <= 10\\) our second requirement is satisfied.

# COMMAND ----------

# MAGIC %md
# MAGIC Since \\(N\\) (our population size) is approximately 22k, our sample size should be no more than \\(22000 \times  .05 = 1100\\). In our case \\(n < .05N\\) so our third requirement is satisfied. We can use a one parameter Z test. 

# COMMAND ----------

# MAGIC %md
# MAGIC # Approcah
# MAGIC In this paper, we will compare two computational packages, [statsmodels](https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.proportions_ztest.html) and the TI-84 One-Prop-Z-Test to compute the P-value of obtaining a sample of size 52 with greater than .17 white cars.

# COMMAND ----------

from statsmodels.stats.proportion import proportions_ztest

# COMMAND ----------

test_statistic, p_value = proportions_ztest(15, 52, .17, alternative='larger', prop_var=.17)

# COMMAND ----------

test_statistic

# COMMAND ----------

p_value

# COMMAND ----------

# MAGIC %md
# MAGIC These numbers match the following output from the TI-84 calculator:

# COMMAND ----------

displayHTML("""<img src='files/shared_uploads/britter6@student.cccd.edu/ztest_1_.jpg'/>""")

# COMMAND ----------

displayHTML("""<img src='files/shared_uploads/britter6@student.cccd.edu/ztest_2_.jpg'/>""")

# COMMAND ----------

# MAGIC %md
# MAGIC # Conclusion

# COMMAND ----------

# MAGIC %md
# MAGIC Because p < .05, there is sufficient evidence to reject the null hypothesis and support the claim that the proportion of white cars at OCC is greater than .17.
