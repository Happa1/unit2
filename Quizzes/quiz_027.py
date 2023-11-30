def count_letters (my_dict:dict, msg:str) -> dict:
    for letter in msg:
        if letter in my_dict:
            my_dict[letter]+=1

    return my_dict


case1 = count_letters(my_dict={'w':0, 'l':0, 'c':0}, msg="hello world")
print(case1)

