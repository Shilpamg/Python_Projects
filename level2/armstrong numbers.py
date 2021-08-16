def solution(A):
    res=[int(x) for x in str (A)]
    sum=0
    for i in range (len(res)):
        sum=(pow(res[i],len(res)))+sum
    if sum==A:
        return A, "is a armstrong number"
    else:
        return A, "is not armstrong number"
print(solution(153))