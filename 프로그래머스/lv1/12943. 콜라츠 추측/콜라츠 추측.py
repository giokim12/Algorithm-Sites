def solution(num):
    answer = 0
    while True:
        if answer >=500:
            return -1
        elif num%2 ==0:
            answer += 1
            num = num/2
        elif num == 1:
            break
        elif num%2 == 1:
            num = num*3+1
            answer +=1
    
    return answer