import pandas as pd
import numpy as np

contaminants = pd.read_csv('famaeGr10/data/contaminants2.csv', index_col=0)
zipcodes = pd.read_csv('famaeGr10/data/zip_codes2.csv')

df = contaminants.merge(zipcodes, left_on='locations_served', right_on='county')

df.dropna()
df.fillna("0.0 ppb", inplace=True)
df['health_limit'][ df['health_limit'].str.contains('non-enforceable health') ] = "0.0 ppb"

print(df['health_limit'].loc[[701859]])
health_limit = df['health_limit'].dropna()
health_limit.fillna("0.0")
average_result = df['average_result'].dropna()
average_result.fillna("0.0")

print(health_limit)

savg = "0.11 ppm"
smax = "100 ppm"

savg_split = savg.split()
smax_split = smax.split()

total = (float(smax_split[0])/float(savg_split[0]))/100
print(total)
