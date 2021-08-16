def fibanacci(n):
    ans=0
    if n<0:
        print("incorrect answer")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        ans= fibanacci(n-1)+fibanacci(n-2)
        return ans
print(fibanacci(6))