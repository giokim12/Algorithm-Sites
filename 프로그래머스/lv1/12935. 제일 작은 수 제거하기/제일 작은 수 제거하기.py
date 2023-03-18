def solution(arr):
    MIN = min(arr)
    arr.remove(MIN)
    if len(arr)==0:
        return [-1]
    else:
        return arr