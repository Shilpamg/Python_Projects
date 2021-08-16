def small(x):
    n=len(x)
    x.sort(reverse=True)
    return x[n-1]
print(small([1,1785,9,6,3,2,18]))