#test arduino
import pyfirmata #select standard

from pyfirmata import Arduino
import time

board = Arduino("/dev/cu.usbserial-10")#address find in arduino userserial, file-> examples -> firmata -> standard firmata
print("Success, Connected to Arduino")

data = pyfirmata.util.Iterator(board)
data.start()

LED_13 = board.digital[13]
LED_13mode = pyfirmata.OUTPUT
LED_13.write(0)

LED_10 = board.digital[10]
LED_10mode = pyfirmata.OUTPUT
LED_10.write(0)

LED_7 = board.digital[7]
LED_7mode = pyfirmata.OUTPUT
LED_7.write(0)

LED_5 = board.digital[5]
LED_5mode = pyfirmata.OUTPUT
LED_5.write(0)

a=1
b=1
c=1
d=1

t = 100
while t>0:
    # LED_13.write(1) #turn on
    # time.sleep(0.5) #0.5 second
    # LED_13.write(0)
    # time.sleep(0.5) #0.5 second

    for x in range(16):
        if x%8==0:
            d =not d
        if x%4==0:
            a=not a
        if x % 2 == 0:
            b = not b
        if x%1==0:
            c=not c

        LED_13.write(a)  # turn on
        LED_10.write(b)  # turn on
        LED_7.write(c)  # turn on
        LED_5.write(d)  # turn on
        time.sleep(0.5)  # 0.5 second

        LED_13.write(a)
        LED_10.write(b)
        LED_7.write(c)
        LED_5.write(d)
        time.sleep(0.5)  # 0.5 second

exit()