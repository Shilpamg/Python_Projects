def solution(A,k,n):
    B=A[:(k-n)]+A[(k-n):]
    print(A[:(k-n)])
    print(A[(n-k):])
    print(B)
print(solution([1,2,3,4,5,6,7,8],3,8))