def solution(s):
    answer = True
    temp = 0
    for i in range(len(s)):
        if s[i] == '(':
            temp += 1
        elif s[i] == ')':
            if temp>0:
                temp -= 1
            else: return False
    
    if temp == 0:
        return True
    else: 
        return False