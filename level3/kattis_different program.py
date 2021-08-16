"""Write a program that computes the difference between non-negative integers.

Input
Each line of the input consists of a pair of integers. Each integer is between 0 and 1015 (inclusive). The input is terminated by 
end of file.

Output
For each pair of integers in the input, output one line, containing the absolute value of their difference."""

def solution (n):
    list1=[]
    for i in range (len(n)):
        list1.append(abs(n[i][0]-n[i][1]))
    return list1

lines=[]
while True:
    try:
        lines.append(list(map(int,input().split())))
    except EOFError as e:
        break
list1=solution(lines)
for i in range(len(list1)):
    print(list1[i])