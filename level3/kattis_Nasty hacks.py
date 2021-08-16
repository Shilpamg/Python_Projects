"""You are the CEO of Nasty Hacks Inc., a company that creates small pieces of malicious software which teenagers may use
 to fool their friends. The company has just finished their first product and it is time to sell it. You want to make as 
 much money as possible and consider advertising in order to increase sales. You get an analyst to predict the expected 
 revenue, both with and without advertising. You now want to make a decision as to whether you should advertise or not, 
 given the expected revenues.
Input
The input consists of n cases, and the first line consists of one positive integer giving n. The next n lines each contain
 3 integers, r, e and c. The first, r, is the expected revenue if you do not advertise, the second, e, is the expected 
 revenue if you do advertise, and the third, c, is the cost of advertising. You can assume that the input will follow 
 these restrictions: 1≤n≤100, −106≤r,e≤106 and 0≤c≤106.

Output
Output one line for each test case: “advertise”, “do not advertise” or “does not matter”, indicating whether it is most 
profitable to advertise or not, or whether it does not make any difference."""


def solution(n):
    digit1=0
    digit2=0
    difference=0
    l1='advertise'
    l2='does not matter'
    l3='do not advertise'
    list1=[]
    for i in range(len(n)):
        digit1=n[i][0]
        digit2=n[i][1]-n[i][2]
        if digit2> digit1:
            list1.append(l1)
        elif digit2< digit1:
            list1.append(l3)
        else:
            list1.append(l2)
    return list1

lines=[]
values=0
for i in range (1):
    values=int(input())
for i in range (values):
    lines.append(list(map(int,input().split())))
list1=solution(lines)
for i in range(len(list1)):
    print(list1[i])



