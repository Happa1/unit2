#Quiz 028 SL
def invert (in_dict:int)-> str:
    return {v:k for k,v in in_dict.items()}

case1 = invert(in_dict={'a':1,'b':2,'c':3})
print(case1)

#Quize 028 HL
def invert (in_dict:dict)-> str:
    out_dict = {}
    for key, value in in_dict.items():
        if value not in out_dict:
            out_dict[value] = [key]
        else:
            out_dict[value].append(key)

    return out_dict

# case1 = invert(in_dict={'a':1,'b':2,'c':3})
case1 = invert(in_dict={'q1':True,'q2':False,'q3':True})
print(case1)


