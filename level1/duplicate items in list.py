def solution(A):
    list1=[]
    for i in range(len(A)):
        for j in range (i+1,len(A)):
            if A[i]==A[j]:
                list1.append(A[i])
    return list(set(list1))
    r
print(solution([1,3,1,1,3,4,3,4,1,5,1,6,4]))