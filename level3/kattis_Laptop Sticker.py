def solution(n):
    sub1=abs(n[0]-n[2])
    sub2=abs(n[1]-n[3])
    if sub1>1 and sub2>1:
        return 1
    else:
        return 0
list1=[]
while True:
    try:
        lines=(str(input()))
    except EOFError as e:
        break
list1=(list(lines.split(" ")))
list1=[int(i) for i in list1]
print(solution(list1))