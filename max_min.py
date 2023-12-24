#!/usr/bin/env python3

def find_max(num):
    max=0
    for i in num:
        if i > max:
           max=i         
    print(f"{max}")
    min=max
    for j in num:
        if min > j:
           min=j 
    print(f"{min}")
    sum=min+max
    print(f"{sum}") 

num=[1,2,3,4,5,6,7,8]
find_max(num)
