def solution (a):

    if a==a[::-1]:
        print("palindrom")
    else:
        print("notpalindrom")
    
print(solution("maaym"))