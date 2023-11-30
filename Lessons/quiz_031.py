from unit2_lib import get_sensor, smoothing, smoothing2
import matplotlib.pyplot as plt



sensor1 = get_sensor()
sensor2 = get_sensor(id=2)
# x,y = smoothing(x=sensor1, size_window=5)
# x1,y1 = smoothing2(x=sensor2, size_window=4)


plt.subplot(4,1,1)
plt.xlabel("sensor1 temperature")
plt.ylabel("temperature")
plt.plot(sensor1)

plt.subplot(4,1,2)
plt.xlabel("sensor2 temperature")
plt.ylabel("temperature")
plt.plot(sensor2)

sensor3 = []
for i in range(len(sensor1)):
    sensor3.append(sensor1[i] + sensor2[i])
# for i in range(len(sensor1)):
#     a = sensor1[i]
#     b = sensor2[i]
#     sensor3 = [a+b for a, b in zip(a, b)]


plt.subplot(4,1,3)
plt.xlabel("The sum of the temperature of sensor1 and sensor2")
plt.ylabel("the sum temperature")
plt.plot(sensor3, color="orange")

sensor4 = []
for i in range(len(sensor1)):
    sensor4.append((sensor1[i] + sensor2[i])/2)

plt.subplot(4,1,4)
plt.xlabel("The sum of the temperature of sensor1 and sensor2")
plt.ylabel("the sum temperature")
plt.plot(sensor3, color="red")

plt.show()