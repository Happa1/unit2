import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

fig = plt.figure(figsize=(8,8))

x1 = np.linspace(-6,0,100)
y1 = (x1+2)**2
plt.plot(x1, y1, label="Parabola 1")

x2 = np.linspace(0,6,100)
y2 = (x2-2)**2
plt.plot(x2, y2, label="Parabola 2")

y3 = -(x1+2)**2
plt.plot(x1, y3, label="Parabola 3")

y4 = -(x2-2)**2
plt.plot(x2, y4, label="Parabola 4")

plt.legend()
plt.xlim(-17,17)
plt.ylim(-17,17)
plt.title("Four Funny Parabolas")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()