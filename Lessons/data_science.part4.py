from unit2_lib import get_sensor, smoothing, smoothing2
import matplotlib.pyplot as plt

sensor1 = get_sensor()
sensor2 = get_sensor(id=2)
x,y = smoothing(x=sensor1, size_window=5)
x1,y1 = smoothing2(x=sensor2, size_window=4)


plt.subplot(3,1,1)
plt.plot(sensor1)

plt.subplot(3,1,2)
plt.plot(x,y)

plt.subplot(3,1,3)
plt.plot(x1,y1)

plt.show()