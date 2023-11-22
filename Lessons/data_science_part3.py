import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

#step 1: read data
heart_rate = []
with open("health.csv", "r") as f:
    header = f.readline() # read one line
    data = f.readlines() # read all the other lines

print(header)
print(data)

time = []
t = 0
for d in data:
    sub1, sub2, sub3 = d.strip().split(',')
    heart_rate.append([int(sub1), int(sub2), int(sub3)])
    time.append(t)
    t += 1

print(heart_rate)

#step 2: statistics
mean = []
std = []
min_hr = []
max_hr = []
for v in heart_rate:
    mean.append(np.mean(v))
    std.append(np.std(v))
    min_hr.append(np.min(v))
    max_hr.append(np.max(v))

print(mean, std)

#step 3: visualize
plt.errorbar(time, mean, std, fmt="o", color="#023047")
plt.xlabel("Time(hours)")
plt.ylabel("Hear Rate (pulses per minute)")
plt.fill_between(time, max_hr, min_hr, alpha=0.5, linewidth=0, color="#8ecae6")
plt.show()