import sys
input = sys.stdin.readline
n, m = map(int, input().split())
s = [0]
s_ = []
for i in range(n):
    a = input().strip()
    s.append(a)
    s_.append([a, i + 1])
s_.sort()
for i in range(m):
    a = input().strip()
    if a.isdigit()==True: print(s[int(a)])
    else:
        low, high = 0, n
        while low <= high:
            mid = (low + high) // 2
            if s_[mid][0] < a: low = mid + 1
            else: high = mid - 1
        print(s_[high + 1][1])