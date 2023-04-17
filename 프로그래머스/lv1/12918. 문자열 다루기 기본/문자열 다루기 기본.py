def solution(s):
    flg = 0
    if len(s)==4 or len(s)==6:
        for i in range(len(s)):
            if s[i] == '0' or s[i] =='1' or s[i] =='2' or s[i] =='3' or s[i] =='4' or s[i] =='5' or s[i] =='6' or s[i] =='7' or s[i] =='8' or s[i] =='9':
                flg += 1
    print(flg) 
    if flg == len(s):
        return True
    else: return False
            
    