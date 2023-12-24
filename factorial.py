#!/usr/bin/env python3


def factorial(num):
    fac=1
    i=0
    nums=[]
    while i < int(num):
        nums.append(int(num))
        num=int(num)-1
    print(f"{nums}")
    while i < len(nums):
       fac=nums[i]*fac
       i+=1
    print(f"{fac}")


num=input("ENTER NUM:\n")
factorial(num)

