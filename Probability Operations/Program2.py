# Normal Distribution
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics

# Plot between -10 and 10 with 0.001 steps.
x_axis = np.arange(-10,10,0.001)

# Calculating mean and standard deviation
mean = statistics.mean(x_axis)
sd = statistics.stdev(x_axis)
print("Mean:-", mean)
print("Standard Deviation:-", sd)

# Plotting of Data
plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
plt.show()