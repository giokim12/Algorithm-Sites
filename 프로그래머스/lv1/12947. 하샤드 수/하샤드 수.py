def solution(x):
    temp = str(x)
    div = 0
    for i in range(len(temp)):
        div += int(temp[i])
    
    if x%div ==0:
        return True
    else:
        return False