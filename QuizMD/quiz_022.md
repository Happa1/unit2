# Quiz022
![2023  Quizzes (8)](https://github.com/Happa1/unit1-2024/assets/142579414/6fefc6a8-4d67-4753-b042-db24081182be)

Fig. 1 prompt of quiz 022

## 1.flow of chart
![Computer Science quiz (13)](https://github.com/Happa1/unit1-2024/assets/142579414/af3bc06e-e39f-40d3-b318-92ffe74a93a5)

Fig. 2 algorithm flow chart of quiz 022

## 2.solution
```.py
from matplotlib import pyplot as plt

def produce ():
    x = -10
    y = 0
    x_out=[]
    y_out=[]
    for _ in range(100):
        # x=random.randint(0,100)
        y = 2 * (x + 5) ** 2
        x_out.append(x)
        y_out.append(y)
        x += 0.2

    return y_out, x_out

y,x=produce()

plt.plot(x, y)
plt.xlabel("x", fontsize=20)
plt.ylabel("$y=2*{x+5}^2$", fontsize=20)
plt.show()
```

## 3.proof of work
<img width="660" alt="Screenshot 2023-11-16 at 21 07 38" src="https://github.com/Happa1/unit1-2024/assets/142579414/36f8226f-36c0-41a2-b504-e67c48cf71c0">

Fig. 3 test of quiz 022

## circuit
![IMG_0176](https://github.com/Happa1/unit1-2024/assets/142579414/1efceb56-70e2-41d7-a12e-18c67f44881d)

Fig. 4 circuit of quiz 022