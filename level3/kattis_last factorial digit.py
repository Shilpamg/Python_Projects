"""The factorial of N, written as N!, is defined as the product of all the integers from 1 to N. For example, 
3!=1×2×3=6. This number can be very large, so instead of computing the entire product, just compute the last digit of N! 
(when N! is written in base 10).

Input
The first line of input contains a positive integer 1≤T≤10, the number of test cases. Each of the next T lines contains a 
single positive integer N. N is at most 10.

Output
For each value of N, print the last digit of N!."""


def solution(n):
    list1=[]
    lastdigit=[]
    for i in range(len(n)):
        product1=1
        for j in range(1,n[i]+1):
            product1=product1*j
        list1.append(product1)
    for i in range(len(list1)):
        res = [int(x) for x in str(list1[i])]
        lastdigit.append(res[-1])
    return lastdigit
    
lines=[]
for i in range(1):
    value=int(input())
for i in range (value):
    lines.append(int(input()))
lastdigit=solution(lines)
for i in range(len(lastdigit)):
    print(lastdigit[i])