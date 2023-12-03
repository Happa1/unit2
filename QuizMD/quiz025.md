# Quiz 025
![quiz025.jpg](..%2FAssets%2Fprompt%2Fquiz025.jpg)
**Fig.1:** prompt of quiz 025

## 1. flow of chart
![quiz025_diagram.jpg](..%2FAssets%2Fdiagram%2Fquiz025_diagram.jpg)
**Fig.2:** algorithm flow chart of quiz 025

## 2. solution
```.py
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
```

## 3. Proof of work
![quiz025_evidence.png](..%2FAssets%2Fevidence%2Fquiz025_evidence.png)
**Fig.3:** Evidence for quiz 025