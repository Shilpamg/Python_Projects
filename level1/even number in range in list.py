def solution(A):
    list1=[]
    for i in range(len(A)):
        if A[i] % 2==0:
            list1.append(A[i])
            print(list1)
    list1.sort()
    return list1
print(solution([1,6,9,2,4,5,3,5,6,7,8]))