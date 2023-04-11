def solution(price, money, count):
    times = 0
    answer = 0
    for i in range(1, count+1):
        times += i
    
    answer = price*times-money
    if answer > 0:
        return answer
    else: return 0