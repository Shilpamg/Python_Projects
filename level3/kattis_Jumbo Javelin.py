def solution(n):
    sum=0
    result=0
    for i in range(len(line)):
        sum=sum+line[i]
    result=sum-(value-1)
    return result
line=[]
value=int(input())
for i in range (value):
    line.append(int(input()))
print(solution(line))

