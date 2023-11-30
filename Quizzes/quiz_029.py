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