# Quiz 024
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

h = [57.0, 56.0, 57.0, 56.0, 55.0, 55.0, 54.0, 54.0, 54.0,
     53.0, 53.0, 54.0 , 53.0, 53.0, 52.0, 52.0, 51.0, 51.0,
     50.0, 50.0, 49.0, 50.0, 49.0, 49.0, 48.0, 48.0, 49.0, 49.0,
     48.0, 48.0, 48.0, 49.0]
print(len(h))

time=[]
t=0

for i in range(len(h)):
     time.append(t)
     t += 10

plt.scatter(time, h, color="blue")
plt.xlabel("Time (min)")
plt.ylabel("Humidity (%)")

m, b =np.polyfit(time, h, 1) # 1 degree
print(f"Linear model H(h) = {m:.2f}t+{b:.2f}")

time_model = []
h_model = []
t = 0
for i in range(len(h)):
    time_model.append(t)
    h_model.append(m*t + b)
    t += 10  #5min

plt.plot(time_model, h_model, color="black")
plt.text(1, 4,f"H(h) = {m:.2f}t+{b:.2f}", fontsize=20)
plt.show()