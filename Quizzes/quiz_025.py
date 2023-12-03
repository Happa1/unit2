# Quiz 025
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

sensorA = [16,24,24,9,23,26,26,23,25,14]
sensorB = [2,19,25,10,11,27,17,7,24,17]
sensorC =[15,11,24,21,6,2,18,27,1,16]


time = []
total = []
mean = []
std = []
min = []
max = []

for t in range(len(sensorA)):
    total.append([int(sensorA[t]), int(sensorB[t]), int(sensorC[t])])
    time.append(t)
    t += 1

for i in total:
    mean.append(np.mean(i))
    std.append(np.std(i))
    min.append(np.min(i))
    max.append(np.max(i))

print(mean, std)


plt.errorbar(time, mean, std, fmt="o", color="#023047")
plt.xlabel("Time")
plt.ylabel("Sensor")
plt.fill_between(time, max, min, alpha=0.5, linewidth=0, color="#8ecae6")
plt.show()