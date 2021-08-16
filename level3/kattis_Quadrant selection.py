def solution(a,b):
    if a>0 and b>0:
        return 1
    elif a<0 and b>0:
        return 2
    elif a<0 and b<0:
        return 3
    elif a>0 and b<0:
        return 4
    elif a==0 or b==0:
        return None
lines=[]
while True:
    try:
        lines.append(int(input()))
    except  EOFError as e:
        break
print(solution(lines[0],lines[1]))
