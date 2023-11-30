import matplotlib.pyplot as plt
import requests
import numpy as np

def get_sensor(id:int=1, ip:str="192.168.6.153"):
    request = requests.get(f'http://{ip}/readings')
    data = request.json()
    sensors=data['readings'][0]
    sensor = []
    x = []
    start = 0

    for s in sensors:
        if s['sensor_id']==id:
            sensor.append(s['value'])
            x.append(start)
            start += 1
    print(sensor)
    print(len(sensor))
    print(x)
    print(len(x))

    return sensor, x

def smoothing(x:list[int], size_window:int=5):
    smooth_x = []
    t = []
    print(f"len_x:{len(smooth_x)}")
    for i in range(0, len(x), size_window):
        points=sum(x[i : i + size_window]) / size_window
        smooth_x.append(points)
        t.append(i)
    # smooth_x = x[200:400]
    # t=x[200:400]
    print(f"len_smooth_x:{len(smooth_x)}")

    return t, smooth_x

sensor1, t = get_sensor(id=2)

print(len(sensor1))
x,y = smoothing(x=sensor1[200:400], size_window=5)
print(len(y))
# sect_y = y[200:400]
# sect_x = x[200:400]

p =np.polyfit(x, y, 2) # 1 degree
# print("3次関数式係数 : %s"%(p))
print(f"Linear model T(t) = {t[0]:.2f}t^2+{t[1]:.2f}t+{t[2]:.2f}")

Figure, ax = plt.subplots()
# plt.subplot(3,1,1)
# plt.plot(sect_x,sect_y)
plt.plot(x,y)
# plt.subplot(3,1,2)
# plt.plot(x,y)

plt.show()