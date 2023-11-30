# listening_arduino
## Nov 22, 2023

import serial
import matplotlib.pyplot as plt

id = "cu.usbserial-10"

arduino = serial.Serial(port=f"/dev/{id}",
                        baudrate=9600, timeout=0.1)

def read():
    data = ""
    while len(data)<1:
        data = arduino.readline()
        return data.decode('utf-8') #utf-8 same name for ascii

time = 0
time_list = []
humidity = []
temperature = []

for i in range(100):
    msg = read()
    print(msg)
    if "Humidity" and "Temperature" in msg:
        msg_split = msg.split(' ')
        # print(msg_split)
        hum = msg_split[0].split(':')
        # print(hum)
        hum = hum[1].strip('%')
        # print(hum)

        temp_split = msg_split[1].split(':')
        temp = temp_split[1].strip().strip('C')

        time += 1
        humidity.append(hum)
        temperature.append(temp)
        time_list.append(time)
        print(humidity)
        print(temperature)
        print(time_list)

plt.style.use('ggplot')
plt.subplot(2,1,1)
plt.plot(time_list, humidity, color='r', marker="*")

plt.subplot(2,1,2)
plt.plot(time_list, temperature, color='black', marker="*")

plt.show()


# print(msg)

