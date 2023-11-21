# SL quiz 017
def get_l3tt3r (msg:str)->str:
    output=""
    for i in msg:
        if i=="a":
            output+="4"
        elif i=="e":
            output+="3"
        elif i=="i":
            output+="1"
        elif i=="o":
            output+="0"
        elif i==" ":
            output+="_"
        else:
            output+=i

    return output

case1=get_l3tt3r(msg="Hello World")
print(case1)

# HL quiz 017
def get_l3tt3r (msg:str)->str:
    letter = {"a":"4", "e":"3","i":"1","o":"0"," ":"_"}
    output = ""
    for i in msg:
       output += letter.get(i, i)
    return output

case1=get_l3tt3r(msg="Hello World")
print(case1)



