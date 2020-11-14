import pandas as pd
import sys


df=pd.read_csv(sys.argv[1])
print(df.columns)
print(df['Review Count'].mean(axis=0))