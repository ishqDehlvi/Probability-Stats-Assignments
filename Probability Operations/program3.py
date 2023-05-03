# Plot Normal Distribution graph for IRIS Dataset

import pandas as pd
df=pd.read_csv("insert_path_here") #put the path here of the iris dataset 
print(df)
df.head(6)
df.tail(6)
df.columns
df.size
df.info()
data=df['sepal.length']
#calculate mean of each numeric column
print(data.mean())
print(data.mode())
print(data.median())
import statistics
print(statistics.stdev(data))
#calculate mean of numeric column
print(df.mean(numeric_only=True))
#calculate median of numeric column
print(df.median(numeric_only=True))  
#calculate mode of numeric column
print(df.mode(numeric_only=True))
import matplotlib.pylot as plt
from scipy.stats import norm

x_axis=data
sd=statistics.stdev(data)
mean=statistics.mean(data)
plt.plot(x_axis,norm.pdf(x_axis,mean,sd))
plt.show()
