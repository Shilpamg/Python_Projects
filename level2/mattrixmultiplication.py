def solution (a,b):
    import numpy as np
    row= [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

  
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                row[i][j]=row[i][j]+ (a[i][k]*b[k][j])
    return row
print(solution([[2, 1, 3],
    [4, 3, 2],
    [1, 2, 3]],   
    [[5, 1, 1, 2],
    [6, 2, 3, 0],
    [4, 3, 2, 1]]))