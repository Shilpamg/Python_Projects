def solution(x,y,d):
    count=0
    if x>=y:
        return 0
    count=int(y/d)
    print (count)
    if (count*d)+x>=y:
        count=count
        return count
    
    else:
        count=count+1
        return count
    
print(solution(10,65,30))
 
 while x<y:
        x=x+d
        count=count+1
    return (count)  
