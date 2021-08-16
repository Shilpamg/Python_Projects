def solution(start,end):
    l=[]
    for i in range (start,end+1):
        if i>1:
            for j in range (2,i):
                if i%j==0:
                    break
            else:
                l.append(i)
    print(l)
        
solution(11,25)
        
