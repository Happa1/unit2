# Quiz 18

## Python code
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

## Evidence

![](/Assets/quiz018evidence.png)

**Fig.1:** Evidence for quiz 18