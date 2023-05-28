def solution(k, tangerine):
    answer = 0
    tangerine = sorted(tangerine, key=lambda x: x)
    bucket = [0]*(tangerine[-1] +1)
    for i in range(len(tangerine)):
        bucket[tangerine[i]] += 1   
    bucket = sorted(bucket, key=lambda x: -x)
    for i in range(len(bucket)):
        k -= bucket[i]
        answer += 1
        if k<=0:
            return answer