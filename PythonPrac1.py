import pandas as pd
import numpy as np
df = pd.read_csv('D:\\Python\\test.csv')
print (df['age'].max())
print (df['name'][df['sal'].max()])
# print (df['name'][df['sal']=='12'])