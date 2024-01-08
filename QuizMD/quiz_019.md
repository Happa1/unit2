# Quiz019
![2023  Quizzes (5)](https://github.com/Happa1/unit1-2024/assets/142579414/78dbfd4b-1c1a-4b55-8005-2de090a5b5f6)

Fig. 1 prompt of quiz 019

## 1.flow of chart
![Computer Science quiz (10)](https://github.com/Happa1/unit1-2024/assets/142579414/3079078c-449a-420d-9f9a-d9c8dc23273d)

Fig. 2 algorithm flow chart of quiz 019

## 2.solution
```.py
def get_truth():
    a=1
    b=1
    c=1
    bool=0
    output=f"| A | B | C |AB+ not B + not CB |\n"

    for x in range(8):
        if x%4==0:
            a=not a
        if x % 2 == 0:
            b = not b
        if x%1==0:
            c=not c

        bool=(a and b) or (not b) or (not(c and b))
        output+=f"| {int(a)} | {int(b)} | {int(c)} |         {int(bool)}         |\n"

    return output

table=get_truth()
print(table)
```

## 3.proof of work
<img width="375" alt="Screenshot 2023-11-16 at 20 51 43" src="https://github.com/Happa1/unit1-2024/assets/142579414/647a193e-2785-45d1-816e-cb9701b11af1">

Fig. 3 test of quiz 019

## Truth table and circuit
![IMG_0173](https://github.com/Happa1/unit1-2024/assets/142579414/ee60df8e-f1dc-4ab8-9ca2-94c55ea6964f)

Fig. 4 truth table and circuit of quiz 019