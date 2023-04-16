def solution(sizes):
    answer = 0
    MAXX = 0
    MAXY = 0
    for i in range(len(sizes)):
        sizes[i] = sorted(sizes[i])
        if sizes[i][0]>MAXX:
            MAXX = sizes[i][0]
        if sizes[i][1]>MAXY:
            MAXY = sizes[i][1]
                
    answer = MAXX*MAXY       
    return answer