# Quiz 029
![quiz029.jpg](..%2FAssets%2Fprompt%2Fquiz029.jpg)
**Fig.1:** prompt of quiz 029

## 1. flow of chart
![quiz29_diagram .jpg](..%2FAssets%2Fdiagram%2Fquiz29_diagram%20.jpg)
**Fig.2:** algorithm flow chart of quiz 029

## 2. solution
```.py
# Quiz 029
def sort_dict(in_dict:dict)->str:
    v = list(in_dict.values())
    k = list(in_dict.keys())

    for i in range(len(v)):
        for n in range(i+1,len(v)):
            if v[i] > v[n]:
                v[i], v[n] = v[n], v[i]

            if k[i] > k[n]:
                k[i], k[n] = k[n], k[i]

    dict_out={k: v for k, v in zip(k, v)}
    return  dict_out

case1 = sort_dict(in_dict={'apple':5, 'banana':2, 'orange':8, 'grape':1})
print(case1)
```

## 3. Proof of work
![quiz029_evidence.png](..%2FAssets%2Fevidence%2Fquiz029_evidence.png)
**Fig.3:** Evidence for quiz 029