def solution(A):
    sum=0
    list1=[]
    for i in range (len(A)):
        sum=sum+A[i]
        list1.append(sum)
    return list1
print(solution([1,2,3,4]))

