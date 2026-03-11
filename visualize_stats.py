import numpy as np
import matplotlib.pyplot as plt

data = [0,1,2,3,4,5,6,7,8]

arr = np.array(data)

mean = np.mean(arr)
std = np.std(arr)

plt.figure(figsize=(8,5))
plt.hist(arr, bins=5)

plt.axvline(mean, linestyle='--', label=f'Mean: {mean}')
plt.axvline(mean + std, linestyle=':', label=f'+1 Std Dev')
plt.axvline(mean - std, linestyle=':', label=f'-1 Std Dev')

plt.title("Data Distribution with Mean and Standard Deviation")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.legend()

plt.savefig("distribution_plot.png")
plt.show()
