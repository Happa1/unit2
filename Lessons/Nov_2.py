def fromdecimal (num,base):
    result=""
    d = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    while num>base:
        result=str(num%base)+result
        num=num//base
    if num in range(10,16):
        num=d[num]
    result=str(num)+result
    return result

test=fromdecimal(num=162,base=16)
print(test)
