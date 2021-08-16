def solution(A,n):
    mul=1
    for i in range (len(A)):
        mul=mul*A[i]
    return mul%n
    
print(solution([100, 10, 5, 25, 35, 14],11))
