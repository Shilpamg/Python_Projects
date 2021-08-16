a=[1,2,3,4,5,6,7,8,9]
b=[1,4,6,9,11]
common=[]
for i in range(len(a)):
    for x in range(len(b)):
        if a[i]==b[x]:
            common.append(a[i])
print(common) 