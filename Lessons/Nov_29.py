# Nov 29
# composite plots

from matplotlib.gridspec import GridSpec
from unit2_lib import get_sensor, smoothing
import matplotlib.pyplot as plt
import matplotlib

plt.style.use('ggplot')
matplotlib.use('MacOSX')

#step1 get sensors
sensors = []
for s in [0,1,2,3]:
    data = get_sensor(id=s)
    sensors.append(data)
    print(f"Sensor {s} obtained with {len(data)} samples")

num_samples = len(sensors[1])
average = []
for i in range(num_samples):
    total = 0
    for s in sensors:
        total += s[i]
    average.append(total/len(sensors))

fig = plt.figure(figsize=(10,8))
grid = GridSpec(3, 3, figure = fig)

box1 = fig.add_subplot(grid[0:2, 0:2])
plt.plot(average, color="red")
plt.title("Average of all sensors")

box2 = fig.add_subplot(grid[0,2])
plt.plot(sensors[0], color="black")
plt.title("Sensors id=0")

box3 = fig.add_subplot(grid[1,2])
plt.plot(sensors[1], color="black")
plt.title("Sensors id=1")

box4 = fig.add_subplot(grid[2,0])
plt.plot(sensors[2], color="black")
plt.title("Sensors id=2")

box5 = fig.add_subplot(grid[2,1])
plt.plot(sensors[3], color="black")
plt.title("Sensors id=3")

plt.subplots_adjust(wspace=0.5, hspace=0.5)

plt.show()