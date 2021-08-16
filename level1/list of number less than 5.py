lst=[1,2,4,5,6,7,8,9,10]
length=len(lst)
lstless5=[]
for i in range(length):
    if lst[i]<5:
        lstless5.append(lst[i])
print(lstless5)