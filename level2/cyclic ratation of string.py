def solution(list,n):
    list1=list
    list2=[]
    if len(list1)<2:
        print(list1)
    while n>len(list1):
        n=n-len(list1)
    print(n)
    for i in range (n):
        list2.append(list1.pop())
    print(list2)
    list22=list2[::-1]
    print(list22)
    print(list1)
    print(list22+list1)
solution([],1)