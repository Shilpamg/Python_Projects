def solution(A):
    list1=A
    
    list2=[]
    count_pair=0
    for i in range(len(list1)):
        for j in range(len(list1)):
            if list1[i]==list1[j]:
                count_pair=count_pair+1
        if count_pair%2==0:
            count_pair=0
        else:
            count_pair=0
            list2.append(list1[i])
    list2=list(set(list2))
    print(list2)
    for x in list2:
        yield x
    
solution([1,2,3,4,5,0,1,2,4,5,1,0])
        
            

