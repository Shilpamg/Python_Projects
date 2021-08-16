"""Rearrenge the  5 in given number to get highest value"""

#! /usr/bin/python3
import sys
def solution (a):
    list1=list(a)
    list2=list(set(list1))
    print(list2)
    list2_product=1
    list1_product=1
    for i in range(1,len(list1)+1):
        list1_product=list1_product*i
    print(list1_product)
    for i in range (len(list2)):
        count=0
        for j in range(len(list1)):
            if list2[i]==list1[j]:
                count=count+1
        while count>1:
            list2_product=list2_product*count
            count=count-1
    print(list2_product)
    result=list1_product//list2_product
    return result

line = []
for i in range(1):  
    try:
        line.append(str(input()))
    except  EOFError as e:
        break
for i in range(len(line)):
    print(solution(line[i]))
"""    
    
except EOFError as e:
    print(e)
    if line=="":
        exit
    else:
        print(solution(line)) """
    
""" for line in sys.stdin:
    print(solution(line)) """

