game = {"Today is Monday": "No",
        "I am bob": "No"}

for question in game.keys():
    print(question)
    answer = None
    while not answer or answer not in ["Yes", "No"]:
        answer = input("enter Yes/No")
    print(f"your answer is {answer}")

    if answer == game[question]:
        print("you are correct")
    else:
        print("not correct")