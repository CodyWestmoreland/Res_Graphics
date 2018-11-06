import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Code records and plots the difference between arithmatic and harmonic mean as scaled by two variables
# The idea is a quick visualization of the harmonic mean's sensitivity to each variable

Sample_size = np.zeros([3,10000])
Number_size = np.zeros([3,10000])
Constants = [3,11,101]

# Increases sample size and records difference
for i in range(3):
    for j in range(1,10001):
        Numbers = np.random.randint(1,Constants[i], size = j)
        Sample_size[i,j-1] = np.mean(Numbers) - stats.hmean(Numbers)

# Increases Number size and records difference
for i in range(3):
    for j in range(2,10002):
        Numbers = np.random.randint(1,j, size = Constants[i])
        Number_size[i,j-2] = np.mean(Numbers) - stats.hmean(Numbers)

plt.subplot(211)
plt.title('Increasing Sample Size with Three fixed Number variabilities')
plt.ylabel('Arithmetic Mean - Harmonic Mean')
plt.xlabel('Sample Size')
plt.plot(range(1,10001),Sample_size[0])
plt.plot(range(1,10001),Sample_size[1])
plt.plot(range(1,10001),Sample_size[2])

plt.subplot(212)
plt.title('Increasing Number Variability with Three Fixed Sample Sizes')
plt.ylabel('Arithmetic Mean - Harmonic Mean')
plt.xlabel('Largest Number')
plt.plot(range(1,10001),Number_size[0])
plt.plot(range(1,10001),Number_size[1])
plt.plot(range(1,10001),Number_size[2])
plt.show()
