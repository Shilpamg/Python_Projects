def solution(A):
    exponent=0
    squreroot=0
    counter=0
    length=len(A)
    i=0
    import math
    while length>1:
        for j in range(i+1,length): 
            squreroot=math.sqrt((i-j)**2)
            if squreroot>A[j]+A[i] or squreroot<A[i]-A[j] or squreroot<A[i]-A[j]:
                counter=counter+1
        
        A.remove(A[i])
        print(A)
        length=length-1
        i=i+1
        print(counter)
                
print(solution([1,5,2,1]))