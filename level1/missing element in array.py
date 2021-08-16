def solution (A):
    A.sort()
    for i in range (len(A)):
        if A[i+1]==A[i]+1:
            continue
        else:
            return A[i]+1
print(solution([1,2,4,5,9,7,3]))
