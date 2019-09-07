import pandas as pd
import numpy as np

# df is DataFrame
df = pd.read_csv('E:\\Python\\test.csv')

# Preview the first 5 lines of the loaded data
# print(df.head())

#print the max age
print ("Maximum age in data frame : ", df['age'].max())

# Who got max salary ?
print("The person who got max salary \n", df[df.sal == df.sal.max()])

