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