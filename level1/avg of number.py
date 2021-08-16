number=int(input("enter number: "))
avg=0
total=0
for i in range(number+1):
    total=i+total
print(total)
avg=total/number
print(avg)