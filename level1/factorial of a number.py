def factorial(x):
    if x<=1:
        return x
    y=1
    for i in range (1,x+1):
        y=i*y
    return y
print(factorial(14))