N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr = sorted(arr, key=lambda x: (x[1], x[0]))

for i in range(N):
    for j in range(2):
        print(arr[i][j], end=' ')
    print()