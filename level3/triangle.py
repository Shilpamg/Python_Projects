def solution(A):
    A.sort()
    print(A)
    sum=0
    sum1=0
    sum2=0
    for x in range(5, len(A)-1):
        print(x)
    for i in range(len(A)-1):
        sum=A[i]+A[i+1]
        for j in range(i+2,len(A)):
            print(f"value of j is {j} when i is {i}")
            if sum>A[j]:
                sum1=A[i]+A[j]
                if sum1>A[i+1]:
                    sum2=A[i+1]+A[j]
                    if sum2>A[i]:
                        return 1
    
    return 0

print(solution([2,5,1,8,3]))