def solution(A,d,n):
    A=A[(n-d):]+A[:(n-d)]
    return A
print(solution([1,3,4,7,2,6],4,6))

