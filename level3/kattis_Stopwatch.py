"""Robin just received a stopwatch from her grandfather. Robin’s stopwatch has a single button. Pressing the button 
alternates between stopping and starting the stopwatch’s timer. When the timer is on, the displayed time increases by 1 
every second.Initially the stopwatch is stopped and the timer reads 0 seconds. Given a sequence of times that the
stopwatch button is pressed, determine what the stopwatch’s timer displays.

Input
The first line of input contains a single integer N (1≤N≤1000), which is the number of times the stopwatch was pressed.
The next N lines describe the times the stopwatch’s button was pressed in increasing order. Each line contains a single 
integer t (0≤t≤106), which is the time the button was pressed. No two button presses happen on the same second.

Output
Display still running if the stopwatch’s timer is still running after all button presses were made. Otherwise display the
number of seconds displayed on the stopwatch’s timer """

def solution(n):
    b=n[::2]
    c=n[1::2]
    sum=[]
    sum1=0
    length1=len(n)
    if length1%2!=0:
        return "still running"
    else:
        for i in range(len(b)):
            sum.append((c[i]-b[i]))
        for i in range(len(sum)):
            sum1=sum1+sum[i]
    return sum1
line = []
for i in range(1):  
    values=(int(input()))
for i in range(values):
    line.append(int(input()))
     
print(solution(line))

