def sumofsquare(n):
    sum=0
    
    square=1
    for i in range(n+1):
        square=(i*i)
        
        sum=sum+square
    return sum
print(sumofsquare(3))
    