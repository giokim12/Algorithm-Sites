def solution(k, m, score):
    answer = 0
    score = sorted(score, key=lambda x: -x) # 내림차순으로 정렬
    box_number = len(score)//m # 박스 개수
    for i in range(box_number):
        answer += score[(i+1)*m-1] * m    
    return answer