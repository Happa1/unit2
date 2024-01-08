# Quiz 34
![quiz034.png](..%2FAssets%2Fprompt%2Fquiz034.png)
**Fig.1:** prompt of quiz 34

## 1. flow of chart

**Fig.2:** algorithm flow chart of quiz 34

## 2. solution
```.py
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
```

## 3. Proof of work
![quiz034_evidence.png](..%2FAssets%2Fevidence%2Fquiz034_evidence.png)
**Fig.3:** Evidence for quiz 34