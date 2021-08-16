def fibanacci(a):
    n1=0
    n2=1
    n3=0
    if a<0:
        print("incorrect answer")
    else:
        for i in range(a+1):
            print (n1)
            n3=n2+n1
            n1=n2
            n2=n3

print(fibanacci(7))