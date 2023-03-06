def solution(n, words):
    flg = 0
    turn = 0
    who = 0
    answer = []
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1]:
            if (i+1)%n==0:
                turn = (i+1)/n
                who = n
            else:
                turn = i//n +1
                who = (i+1)%n
            answer.append(who)
            answer.append(turn)
            flg = 1
            return answer
        elif words[i] in words[:i-1]:
            flg = 1            
            if (i+1)%n==0:
                turn = (i+1)/n
                who = n
            else:
                turn = i//n +1
                who = (i+1)%n
            answer.append(who)
            answer.append(turn)
            return answer
        else:
            continue
    
    if flg == 0:
        return [0,0]

    