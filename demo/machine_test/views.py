from doctest import master
from django.shortcuts import render
from django.http import HttpResponse



s='aabcglactdge'
ls=list(s)
l=['cat','bat','egg','ball']
cnt=0
for i in l:
    d=list(i)
    for j in d:
        if j in ls:
            cnt+=1
            ls.remove(j)
    if len(d)==cnt:
        print('yes')
    else:
        print("no")
        cnt=0
print(ls)