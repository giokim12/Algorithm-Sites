def solution(s):
    used = []
    answer = []
    for i in range(len(s)):
        if s[i] not in used:
            used.append(s[i])
            answer.append(-1)
        else:
            temp = 1
            for j in range(i-1, -1, -1):
                if s[j] == s[i]:
                    answer.append(temp)
                    break
                else: 
                    temp += 1
                
    return answer