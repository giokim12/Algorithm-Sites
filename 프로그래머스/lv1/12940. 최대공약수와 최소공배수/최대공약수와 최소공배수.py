def solution(n, m):
    answer = []
    if n<m:
        for i in range(n, 0, -1):
            if m%i == 0 and n%i == 0:
                answer.append(i)
                break
        for j in range(m, m*n+1):
            if j%n == 0 and j%m == 0:
                answer.append(j)
                break
    else:
        for i in range(m, 0, -1):
            if m%i == 0 and n%i == 0:
                answer.append(i)
                break
        for j in range(n, m*n+1):
            if j%n==0 and j%m == 0:
                answer.append(j)  
                break
    
    return answer
                
                