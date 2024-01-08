# Quiz 35

**Fig.1:** prompt of quiz 35

## 1. flow of chart

**Fig.2:** algorithm flow chart of quiz 35

## 2. solution
```.py
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

fig = plt.figure(figsize=(10,8))

x1 = np.linspace(-1.00,1.00,100)
y1 = -(x1)**2+2
plt.plot(x1, y1, label="Parabola", c='green')

x2 = np.linspace(-1.00,0,100)
y2 = -x2*2-1
plt.plot(x2, y2, label="left line", c='red')

x3 = np.linspace(0,1.00,100)
y3 = x3*2-1
plt.plot(x3, y3, label="right line", c='blue')

plt.legend(loc='lower left')
plt.xlim(-1.05,1.05)
plt.ylim(-1.05,2.05)
plt.title("Cone Shapre Graph with Parabolas ans Lines")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```

## 3. Proof of work
![quiz035_evidence.png](..%2FAssets%2Fevidence%2Fquiz035_evidence.png)
**Fig.3:** Evidence for quiz 35