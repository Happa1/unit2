import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

#imaginary temperatire taken every 5 min
temp=[1.5, 1.5, 2.0, 2.8, 3.2, 4.0, 5, 5, 6.0]
time=[]
t=0
for i in range(len(temp)):
    time.append(t)
    t += 5 # 5min

plt.scatter(time, temp, color="blue")
plt.xlabel("Time (min)")
plt.ylabel("Temperature (C)")

m, b =np.polyfit(time, temp, 1) # 1 degree
print(f"Linear model T(t) = {m:.2f}t+{b:.2f}")

time_model = []
temp_model = []
t = 0
for i in range(len(temp)):
    time_model.append(t)
    temp_model.append(m*t + b)
    t += 5  #5min

plt.plot(time_model, temp_model, color="black")
plt.text(1, 4,f"T(t) = {m:.2f}t+{b:.2f}", fontsize=20)
plt.show()

#use the model to predict the temp 5 minutes in the future
temp_future = m*(45) + b
print(f"Prediction Linear model {temp_future:.2f}C = {m:.2f}(45min)+{b:.2f}")