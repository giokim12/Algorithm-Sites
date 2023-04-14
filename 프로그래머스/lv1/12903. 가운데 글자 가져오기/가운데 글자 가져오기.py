def solution(s):
    answer = ''
    word_length = len(s)
    print(word_length)
    mid = word_length//2
    print(mid)
    if word_length%2 == 0:
        answer = s[mid-1]+s[mid]

    else: 
        answer =  s[mid]
        
    print(answer)
    return answer