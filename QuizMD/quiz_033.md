# Quiz 33
![quiz033.png](..%2FAssets%2Fprompt%2Fquiz033.png)
**Fig.1:** prompt of quiz 33

## 1. flow of chart
![quiz033_diagram.jpg](..%2FAssets%2Fdiagram%2Fquiz033_diagram.jpg)
**Fig.2:** algorithm flow chart of quiz 33

## 2. solution
```.py
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

fig = plt.figure(figsize=(8,8))

x1 = np.linspace(-4,4,100)
y1 = x1**2
plt.plot(x1, y1, label="Parabola 1 (x-axis)")

x2 = np.linspace(-4,4,100)
y2 = -x2**2
plt.plot(x2, y2, label="Parabola 2 (x-axis)")

x3 = np.linspace(-4,4,100)
y3 = x3**2
plt.plot(y3, x3, label="Parabola 3 (y-axis)")

x4 = np.linspace(-4,4,100)
y4 = -x4**2
plt.plot(y4, x4, label="Parabola 4 (y-axis)")

plt.legend()
plt.xlim(-4.5,4.5)
plt.ylim(-4.5,4.5)
plt.title("Four Parabolas Aligned with Axes")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()
```

## 3. Proof of work
![quiz033_evidence.png](..%2FAssets%2Fevidence%2Fquiz033_evidence.png)
**Fig.3:** Evidence for quiz num