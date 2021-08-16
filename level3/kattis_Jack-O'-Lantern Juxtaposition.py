def solution(m):
    product=1
    for i in range(len(m)):
        product=product*m[i]
    return product

list1=[]
while True:
    try:
        lines=str(input())
    except EOFError as e:
        break
list1=list(map(int,(list(lines.split(" ")))))
print(solution(list1))

