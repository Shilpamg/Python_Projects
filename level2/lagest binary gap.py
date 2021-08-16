def solution(n):
    binary=format(n,"b")
    print(binary)
    list1=[int(x) for x in str(binary)]
    print(list1)
    length=len(list1)
    count_list=[]
    for i in range (length-1):
        if list1[i]==1:
            count=0
            while list1[i+1]==0:
                count=count+1
                i=i+1
                if i+1<length:
                    continue
                else:
                    count=0
                    break
                print(count)
            count_list.append(count)
    count_list.sort()
    print(count_list)
    print (count_list[-1])

solution(43





