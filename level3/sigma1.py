""" The minimum number of insertion to get consecutiv e1 and 0"""
#! /usr/bin/python3
import sys
def number_of_digits(n):
    if n==0:
        return 1
    count=0
    while n!=0:
        n=n//10
    
        count=count+1
    return count

lines = []
for i in range  (1):
    no_of_lines=int(input())
for i in range(no_of_lines):
    lines.append(int(input()))

for i in range(len(lines)):
    print(number_of_digits(lines[i]))
    
