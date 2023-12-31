import  random

random.seed(1234)
def produce (n:int, m:int, s:int):
    x_out=[]
    y_out=[]
    for _ in range(n):
        x=random.randint(0,100)
        y=x**(0.5*((m/s)**2))
        x_out.append(x)
        y_out.append(y)

    return y_out,x_out

import matplotlib.pyplot as plt

plt.style.use('ggplot')

y,x=produce(n=5, m=3, s=2)

plt.plot(x, y, color='r', marker="*")
plt.xlabel("x", fontsize=20)
plt.ylabel("$y=x^{1/2*m/s}$", fontsize=20)
plt.show()