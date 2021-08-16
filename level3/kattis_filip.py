"""Mirko has a younger brother, Filip, who just started going to school and is having trouble with numbers. To help him get 
the hang of the number scale, his teacher writes two three-digit numbers. She asks Filip to compare those numbers, but
instead of interpreting them with the leftmost most significant digit, he needs to interpret them the other way around, 
 with the most significant digit being the rightmost one. He then has to tell the teacher the larger of the two 
numbers.
Write a program that will check Filip’s answers.
Input
The first and only line of input contains two three-digit numbers, A and B. A and B will not be equal and will not 
contain any zeroes.
Output
The first and only line of output should contain the larger of the numbers in the input, compared as described in the 
task. The number should be written reversed, to display to Filip how he should read it."""


def solution(a):
    newlist=[]
    for i in range (len(a)):
        newlist.append((a[i][::-1]))
    if newlist[0]>newlist[1]:
        return newlist[0]
    else:
        return newlist[1]

list1=[]
while True:
    try:
        lines=(str(input()))
    except EOFError as e:
        break
list1=(list(lines.split(" ")))
print(solution(list1))




    
  
    



