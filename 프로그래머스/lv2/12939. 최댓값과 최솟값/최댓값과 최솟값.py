def solution(s):
    arr = list(map(int, s.split()))
    arr = sorted(arr)
    for i in range(len(arr)):
        arr[i] = str(arr[i])
    answer = ''
    answer += arr[0]
    answer += ' '
    answer += arr[-1]
    return answer