def solution(a):
    for row in a:
        res=[[a[j][i] for j in range (len(a))]  for i in  range (len(a[0]))]
    return res
print(solution([[1,2],[3,4],[5,6]]))