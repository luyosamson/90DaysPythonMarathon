# Pandas: Pandas is a package used for data manipulation 
# and analysis. It provides tools for working with structured data, 
# including data frames and series, and includes functions for data cleaning,
# filtering, and transformation.

import pandas as pd
#Create a data frame
data={
    "names":["Samson","Mary","Michael","Victor"],
    "age":[34,56,21,43],
    "salary":[20000,45000,18000,34000]
    }

df=pd.DataFrame(data)

avg_salary=df['salary'].mean()

print("Average salary",avg_salary)



#ADDITIONAL PYTHON PACKAGES

# c. Matplotlib: Matplotlib is a package used for data
# visualization in Python. It provides tools for creating various 
# types of plots and charts, including line plots, scatter plots, and histograms.

# d. Scikit-learn: Scikit-learn is a package used for 
# machine learning in Python. It provides tools for data preprocessing, 
# feature selection, model selection, and evaluation.
