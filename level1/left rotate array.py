"""def solution(A,d,n):
    A[:]=A[d:n]+A[0:d]
    return A
print(solution([1,3,4,7,2,6],4,6))"""

"""def solution(A,d,n):
    temp=[]
    result=[]
    for i in range(d):
        temp.append(A[i])
    for i in range (d,n):
        result.append(A[i])
    A=result+temp
    return A
print(solution([1,3,4,7,2,6],4,6))"""

def solution(A,d,n):
    temp=[]
    result=[]
    i=0
    while i<d:
        temp.append(A[i])
        i=i+1
    print(temp)
    i=0
    while d<n:
        result.append(A[d])
        d=d+1
        i=i+1
    print(result)
    A=result+temp
    return A
print(solution([1,3,4,7,2,6],4,6))
