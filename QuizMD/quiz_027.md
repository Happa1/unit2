# Quiz 027

**Fig.1:** prompt of quiz 027
![quiz027.jpg](..%2FAssets%2Fprompt%2Fquiz027.jpg)
## 1. flow of chart
![quiz027_diagram.jpg](..%2FAssets%2Fdiagram%2Fquiz027_diagram.jpg)
**Fig.2:** algorithm flow chart of quiz 027

## 2. solution
```.py
# Quiz 027
def count_letters (my_dict:dict, msg:str) -> dict:
    for letter in msg:
        if letter in my_dict:
            my_dict[letter]+=1

    return my_dict


case1 = count_letters(my_dict={'w':0, 'l':0, 'c':0}, msg="hello world")
print(case1)
```

## 3. Proof of work
![quiz027_evidence.png](..%2FAssets%2Fevidence%2Fquiz027_evidence.png)
**Fig.3:** Evidence for quiz 027