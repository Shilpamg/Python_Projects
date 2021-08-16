lst1=[1,0,0,1,0,1,1,1,1,1,0]
length=len(lst1)
lst01=[0,1]*length
lst10=[1,0]*length
print(lst01)
print(lst10)
count01=0
count10=0
for i in range (length):
    if lst1[i]-lst01[i]!=0:
        count01=count01+1
    else:
        count10=count10+1
print(count01)
print(count10)
if count01>count10:
    lst1=lst10.copy()
else:
    lst1=lst01.copy()
print(lst1)