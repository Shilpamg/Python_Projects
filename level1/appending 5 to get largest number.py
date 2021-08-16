n=input("enter the number: ")
result=[int(x) for x in  str(n)]
print(result)
cnt=1
A=len(result)
for i in range (A):
    if result[i]<5:
        if cnt>0:
            print(result.insert(i,5))
            cnt=cnt-1
    else:
        A=A-1
        if A==0:
            print(result.insert(len(result)+1,5))
integer=("".join([str(x) for x in result]))
print(integer)
