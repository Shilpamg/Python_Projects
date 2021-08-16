def solution (a,b):
    res=[]
    for i in range(len(a)):
        row=[]
        for j in range(len(a[0])):
            row.append(a[i][j]+b[i][j])
            print(row)
        res.append(row)
    return res
print(solution([[1, 2], [3, 4]],[[2, 2], [2, 2]]))