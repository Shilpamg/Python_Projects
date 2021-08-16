def solution(n):
    count=0
    for i in range (len(n)):
        if n[i]<0:
            count=count+1
    return count

while True:
    try:
        values=int(input())
        lines=str(input())
    except EOFError as e:
        break
list1=[]
list1=list(map(int,(lines.split(" "))))
print(solution(list1))


