import numpy as np
import matplotlib.pyplot as plt
import math

# Define the parameters
return_period = 20  # Return period in years
interval = 5       # Interval in years
k=1                #number of events required

# Calculate the average rate of events per return period (lambda)
lmbda = interval / return_period

# Calculate the probability using the Poisson distribution formula
probability = (math.exp(-lmbda) * lmbda**k) / math.factorial(k)

# Print the result
print(f"{probability:.2f}")

# Generate a range of x values
x = np.linspace(0, 5, 1000)  # Adjust the range and number of points as needed

# Calculate the corresponding Gaussian (normal) probability density function
mean = lmbda
std_dev = math.sqrt(lmbda)
pdf = (1 / (std_dev * math.sqrt(2 * math.pi))) * np.exp(-0.5 * ((x - mean) / std_dev)**2)

# Create a smooth curve
plt.plot(x, pdf, label='Gaussian Distribution', color='blue')
plt.xlabel('Number of Events (k)')
plt.ylabel('Probability Density')
plt.title(f'Smooth Probability Distribution: {interval}-year Period with {return_period}-year Return Period')
plt.legend()
plt.grid(True)
plt.savefig("./figs/fig.png",bbox_inches='tight')






