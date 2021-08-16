def solution(A):
    sum=0
    for i in range(len(A)):
        sum=sum+A[i]
    return sum
print(solution([1,2,3]))