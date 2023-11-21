# Quiz 19

## Python code
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

## Evidence

![](/Assets/quiz019evidence.png)

**Fig.1:** Evidence for quiz 19