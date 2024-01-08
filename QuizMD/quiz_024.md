# Quiz024
![2023  Quizzes (10)](https://github.com/Happa1/unit1-2024/assets/142579414/61504ae9-ad2b-4a38-b624-97621da3f50e)

Fig. 1 prompt of quiz 024

## 1.flow of chart
![Computer Science quiz (15)](https://github.com/Happa1/unit1-2024/assets/142579414/a5f03e16-e34f-431d-abd5-2f9a3090b7ef)

Fig. 2 algorithm flow chart of quiz 024

## 2.solution
```.py
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
```

## 3.proof of work
<img width="636" alt="Screenshot 2023-11-16 at 21 13 17" src="https://github.com/Happa1/unit1-2024/assets/142579414/6341bb79-6d04-4694-86cc-7a02ccd2f456">

Fig. 3 test of quiz 024

## convert to hex coder
![IMG_0178 copy](https://github.com/Happa1/unit1-2024/assets/142579414/7d93ac52-79d5-4cfb-8649-7d0de1ac493f)

Fig. 4 convert to hex coder quiz of quiz 024