#quiz 032
from unit2_lib import get_sensor, smoothing, smoothing2
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
plt.style.use('ggplot')

sensor4 = get_sensor(id=4)
sensor5 = get_sensor(id=5)

num_samples = len(sensor4)
sub = []
for i in range (num_samples):
    sub.append(-(sensor4[i]+sensor5[i])/2)

fig = plt.figure(figsize = (10,5))
grid = GridSpec(3,4,figure =fig)

box1 = fig.add_subplot(grid[0:3, 1:3])
plt.plot(sub, color="red")
plt.ylim(-70, -20)
plt.xticks([0,100,200,300,400,500,600,700,800],[0,100,200,300,400,500,600,700,800])
plt.yticks([-70,-60,-50,-40,-30,-20],[None,-60,-50,-40,-30,None])
plt.title("Sensor#4 - Sensor#5")

box2 = fig.add_subplot(grid[1,0])
plt.plot(sensor4, color="black")
plt.ylim(0, 100)
plt.xticks([0,200,400,600,800],[0,200,400,600,800])
plt.yticks([0,50,100],[0,50,100])
plt.title("Sensor id=4")

box3 = fig.add_subplot(grid[1,3])
plt.plot(sensor5, color="black")
plt.ylim(0, 100)
plt.xticks([0,200,400,600,800],[0,200,400,600,800])
plt.yticks([0,50,100],[0,50,100])
plt.title("Sensor id=5")

plt.show()