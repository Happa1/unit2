sensorA = [16,24,24,9,23,26,26,23,25,14]
sensorB = [2,19,25,10,11,27,17,7,24,17]
sensorC =[15,155,24,21,6,2,18,27,1,16]

import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

total = []
mean = []
std = []

for d in range(len(sensorA)):
    total.append([sensorA[d], sensorB[d], sensorC[d]])

for i in total:
    mean.append(np.mean(i))
    std.append(np.std(i))

print(mean, std)