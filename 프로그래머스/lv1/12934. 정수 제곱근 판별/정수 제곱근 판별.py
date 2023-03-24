def solution(n):
    flg = 0
    for i in range(1, n+1):
        if i*i == n:
            flg = 1
            return (i+1)*(i+1)
    if flg == 0:
        return -1
