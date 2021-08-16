number=int(input("enter number: "))
avg=0
total=0
i=0
while i<=number:
    total=i+total
    i=i+1
print(total)
avg=total/number
print(avg)