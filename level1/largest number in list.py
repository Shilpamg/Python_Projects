def large(x):
    n=len(x)
    x.sort()
    return x[n-1]
print(large([1,1785,9,6,3,2,18]))
