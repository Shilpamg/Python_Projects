"""In the popular show “Dinner for Five”, five contestants compete in preparing culinary delights. Every evening one of 
them makes dinner and each of other four then grades it on a scale from 1 to 5. The number of points a contestant gets is 
equal to the sum of grades they got. The winner of the show is of course the contestant that gets the most points.
Write a program that determines the winner and how many points they got.

Input
Five lines, each containing 4 integers, the grades a contestant got. The contestants are numbered 1 to 5 in the order in 
which their grades were given.

Output
Output on a single line the winner’s number and their points, separated by a space. The input data will guarantee that 
the solution is unique."""

def solution(n):
    prev_sum=0
    sum_index=0
    for i in range (len(n)):
        sum=0
        for j in range (len(n[i])):
            sum=sum+n[i][j]
            if sum> prev_sum:
                sum_index=i+1
                prev_sum=sum      
    return sum_index,prev_sum

lines=[]
for i in range (5):
    lines.append(list(map(int,input().split())))
sum_index,prev_sum=solution(lines)
print(sum_index,prev_sum)