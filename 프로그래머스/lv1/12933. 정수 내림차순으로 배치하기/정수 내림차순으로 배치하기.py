def solution(n):
    arr = list(str(n))
    answer = []
    for i in range(len(arr)):
        temp = int(arr[i])
        answer.append(temp)
    answer2 = sorted(answer, key=lambda x: -x)
    answer3 = ''               
    for i in range(len(answer2)):
        answer3 += str(answer2[i])
    return int(answer3)