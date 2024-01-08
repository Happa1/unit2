# Quiz020
![2023  Quizzes (6)](https://github.com/Happa1/unit1-2024/assets/142579414/dab0cf29-d1c4-4290-a48e-e878fb2a1f15)

Fig. 1 prompt of quiz 020

## 1.flow of chart
![Computer Science quiz (11)](https://github.com/Happa1/unit1-2024/assets/142579414/8d1b4e9a-54de-43bd-87a1-2ca72d5f804c)

Fig. 2 algorithm flow chart of quiz 020

## 2.solution
```.py
import random
random.seed(1234)

def produce (n:int, m:int, s:int):
    x=0
    str_x="x"
    str_y=("y(x)")
    first_row=f"|{str_x.center(10)}|{str_y.center(10)}|\n"
    y=0
    output=""

    for i in range(n):
        x = random.randint(0, 100)
        y=x**(1/2*((m/2)**2))
        formatted_y=f"{y:.2f}"
        output+=f"|{str(x).center(10)}|{formatted_y.center(10)}|\n"

    return first_row+output

sample=produce(n=5, m=3, s=2)
print(sample)

```

## 3.proof of work
<img width="274" alt="Screenshot 2023-11-16 at 20 55 33" src="https://github.com/Happa1/unit1-2024/assets/142579414/46aa2c14-332a-4c27-9d96-ec06e7440d68">

Fig. 3 test of quiz 020

## proof
![IMG_0174](https://github.com/Happa1/unit1-2024/assets/142579414/a90c39aa-6af1-4fc9-aac7-f6bd8a9a1beb)


Fig. 4 proof of boolean equation of quiz 020