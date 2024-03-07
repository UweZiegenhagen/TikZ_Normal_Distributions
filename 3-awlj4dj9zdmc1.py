
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm
import pandas as pd

# Define parameters for the skewed normal distribution
a = -10 # Skewness parameter
mean = 0  # Mean of the distribution
std_dev = 1  # Standard deviation of the distribution

# Generate data points for the skewed normal distribution
x = np.linspace(-7, 7, 500)  # Range of x values
y = skewnorm.pdf(x, a, loc=mean, scale=std_dev)  # Skewed normal distribution

#data = np.concatenate((x,y), axis=1)
xs = pd.Series(x).round(3)
ys = pd.Series(y).round(3)-1
df = pd.concat([xs, ys], axis=1, keys=['x','y'])


# Plot the skewed normal distribution
plt.plot(x, y, color='blue')
plt.title('Skewed Normal Distribution')
plt.xlabel('X')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()

with open('3-awlj4dj9zdmc1.txt', 'w') as o:
    for index, row in df.iterrows():
        o.write('(' + str(row['x']) + ',' + str(row['y']) + ') -- '  )