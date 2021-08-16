def solution(A):
    count=len(A)
    count1=len(A)
    for i in range(len(A)-1):
        if A[i]<=A[i+1]:
            count=count-1
        elif A[i]>=A[i+1]:
            count1=count1-1
    if count==1:
        return "array is monotonic"
    elif count1==1:
        return "array is monotonic"
    else :
        return "array is not monotonic"
print(solution([1,2,3,5,5]))


