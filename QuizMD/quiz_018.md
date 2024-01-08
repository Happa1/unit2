# Quiz018
![2023  Quizzes (4)](https://github.com/Happa1/unit1-2024/assets/142579414/845ba1bc-b090-4c67-b3f3-cae687400114)

Fig. 1 prompt of quiz 018

## 1.flow of chart
![Computer Science quiz (9)](https://github.com/Happa1/unit1-2024/assets/142579414/81332907-9616-4646-b10a-25baedb4ea09)

Fig. 2 algorithm flow chart of quiz 018

## 2.solution
```.py
def get_truth():
    a=1
    b=1
    c=1
    output=f"| A | B | C |\n"

    for x in range(8):
        if x%4==0:
            a=not a
        if x % 2 == 0:
            b = not b
        if x%1==0:
            c=not c

        output+=f"| {int(a)} | {int(b)} | {int(c)} |\n"

    return output

table=get_truth()
print(table)
```

## 3.proof of work
<img width="246" alt="Screenshot 2023-11-16 at 20 49 54" src="https://github.com/Happa1/unit1-2024/assets/142579414/0a61e921-6896-449d-a167-813e53bb5ce4">

Fig. 3 test of quiz 018

## truth table
![IMG_0172](https://github.com/Happa1/unit1-2024/assets/142579414/ed422f43-0b08-4189-85e8-1fe4c66376d2)

Fig. 4 truth table of quiz 018