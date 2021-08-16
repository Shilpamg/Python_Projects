def solution(a):
    words=a.split(' ')
    reverse=' '.join(reversed(words))
    return reverse
print(solution("i am shilpa"))