#test arduino
import pyfirmata #select standard

from pyfirmata import Arduino
import time

board = Arduino("/dev/cu.usbserial-10")#address find in arduino userserial, file-> examples -> firmata -> standard firmata
print("Success, Connected to Arduino")

data = pyfirmata.util.Iterator(board)
data.start()
#
Button4 = board.digital[4]
Button4.mode = pyfirmata.INPUT

Button9 = board.digital[9]
Button9.mode = pyfirmata.INPUT

LED = board.digital[3]
LED.mode = pyfirmata.OUTPUT
LED.write(0)


game = {"Today is Monday": "No",
        "I am bob": "No"}

for question in game.keys():
    print(question)
    answer = None

    while Button4.read()==0 or Button9.read()==0:
        time.sleep(5)
        if Button4.read()==1 and game["question"] == "Yes":
            LED.write(1)
        if Button9.read() == 1 and game["question"] == "No":
            LED.write(1)

    #     button_state4 = Button4.read()
    #     button_state9 = Button9.read()
    #     time.sleep(5)
    #     if button_state4 == 1:
    #         answer = "Yes"
    #     if button_state9 == 1:
    #         answer = "No"
    # time.sleep(5)
    #
    # if answer == game[question]:
    #     print("you are correct")
    #     LED.write(1)
    # else:
    #     print("not correct")
    #     LED.write(0)

# while True:
#     button_state = Button.read()
#     if button_state ==1:
#         LED.write(1)
#     else:
#         LED.write(0)

#
# yes = board.digital[4]
# yes.mode = pyfirmata.INPUT
#
# no = board.digital[9]
# no.mode = pyfirmata.INPUT
#
# questions = {"Today is Monday": "No",
#         "I am bob": "No"}
#
# for question in questions.keys():
#     print(question)
#     answer = questions[question]
#     while yes.read() == 0 and no.read() == 0:
#         time.sleep(0.1)
#     if yes.read == 1 and answer == "Yes":
#             print("You are correct!")
#             LED.write(1)
#     elif no.read == 1 and answer == "No":
#             print("You are correct!")
#             LED.write(1)
#     else:
#         print("You are wrong!")
#     time.sleep(1)
#     yes.write(0)
#     no.write(0)
