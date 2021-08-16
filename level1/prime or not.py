def solution(a):
    for i in range(2,a):
        if a%i==0:
            return a,"is not a prime number"
        else:
            return a,"is a prime number"
print(solution(13))