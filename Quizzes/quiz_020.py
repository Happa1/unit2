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
