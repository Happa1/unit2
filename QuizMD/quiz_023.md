# Quiz023
![2023  Quizzes (9)](https://github.com/Happa1/unit1-2024/assets/142579414/54e6c726-e0ac-45ae-beb4-03f044698eb4)

Fig. 1 prompt of quiz 023

## 1.flow of chart
![Computer Science quiz (14)](https://github.com/Happa1/unit1-2024/assets/142579414/96a5761e-6068-4c00-982e-c479018c2adf)

Fig. 2 algorithm flow chart of quiz 023

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
        y =abs(x)
        x_out.append(x)
        y_out.append(y)
        x += 0.2

    return y_out, x_out

y,x=produce()

plt.plot(x, y)
plt.xlabel("x", fontsize=20)
plt.ylabel("$y=|x|$", fontsize=20)
plt.show()
```

## 3.proof of work
<img width="737" alt="Screenshot 2023-11-16 at 21 10 41" src="https://github.com/Happa1/unit1-2024/assets/142579414/b0edb02a-0ed2-4509-9b83-c4c31bdd25cb">

Fig. 3 test of quiz 023

## convert to decimal
![IMG_0178 copy](https://github.com/Happa1/unit1-2024/assets/142579414/f91fc5c0-9b81-4318-8d25-e3f3c1625850)
Fig. 4 convert to decimal quiz of quiz 023