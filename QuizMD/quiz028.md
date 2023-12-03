# Quiz 028
![quiz028.jpg](..%2FAssets%2Fprompt%2Fquiz028.jpg)
**Fig.1:** prompt of quiz 028

## 1. flow of chart
![quiz28_diagram.jpg](..%2FAssets%2Fdiagram%2Fquiz28_diagram.jpg)
**Fig.2:** algorithm flow chart of quiz 028

## 2a. solution SL
```.py
#Quiz 028 SL
def invert (in_dict:int)-> str:
    return {v:k for k,v in in_dict.items()}

case1 = invert(in_dict={'a':1,'b':2,'c':3})
print(case1)
```

## 2b. solution HL
```.py
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
```

## 3. Proof of work
![quiz028_evidence.png](..%2FAssets%2Fevidence%2Fquiz028_evidence.png)
**Fig.3:** Evidence for quiz 028