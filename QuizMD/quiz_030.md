# Quiz 30
![quiz030.png](..%2FAssets%2Fprompt%2Fquiz030.png)
**Fig.1:** prompt of quiz 30

## 1. flow of chart

**Fig.2:** algorithm flow chart of quiz 30

## 2. solution
```.py
import matplotlib.pyplot as plt
import requests
import numpy as np
from unit2_lib import get_sensor, smoothing

sensor1= get_sensor(id=2)

# print(len(sensor1))
x,y = smoothing(x=sensor1[200:400], size_window=5)
print(len(y))

p =np.polyfit(x, y, 2) # 2 degree
print(f"Linear model T(t) = {t[0]:.2f}t^2+{t[1]:.2f}t+{t[2]:.2f}")

Figure, ax = plt.subplots()
# plt.subplot(3,1,1)
# plt.plot(sect_x,sect_y)
plt.plot(x,y)
# plt.subplot(3,1,2)
# plt.plot(x,y)

plt.show()
```

## 3. Proof of work
not available anymore