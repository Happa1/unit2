# Quiz 31
![quiz031.png](..%2FAssets%2Fprompt%2Fquiz031.png)
**Fig.1:** prompt of quiz num

## 1. flow of chart

**Fig.2:** algorithm flow chart of quiz num

## 2. solution
```.py
from unit2_lib import get_sensor, smoothing, smoothing2
import matplotlib.pyplot as plt
plt.style.use('ggplot')


sensor1 = get_sensor()
sensor2 = get_sensor(id=2)
# x,y = smoothing(x=sensor1, size_window=5)
# x1,y1 = smoothing2(x=sensor2, size_window=4)

fig = plt.figure(figsize=(10,10))
plt.subplots_adjust(hspace=0.5)

plt.subplot(4,1,1)
plt.xlabel("sensor1 temperature")
plt.ylabel("temperature")
plt.plot(sensor1, color='orange')

plt.subplot(4,1,2)
plt.xlabel("sensor2 temperature")
plt.ylabel("temperature")
plt.plot(sensor2)

sensor3 = []
for i in range(len(sensor1)):
    sensor3.append(sensor1[i] + sensor2[i])
plt.subplot(4,1,3)
plt.xlabel("The sum of the temperature of sensor1 and sensor2")
plt.ylabel("the sum temperature")
plt.plot(sensor3, color="blue")

sensor4 = []
for i in range(len(sensor1)):
    sensor4.append((sensor1[i] + sensor2[i])/2)

plt.subplot(4,1,4)
plt.xlabel("The average of the temperature of sensor1 and sensor2")
plt.ylabel("the average temperature")
plt.plot(sensor4, color="black")

plt.show()
```

## 3. Proof of work
![quiz031_evidence.png](..%2FAssets%2Fevidence%2Fquiz031_evidence.png)
**Fig.3:** Evidence for quiz num