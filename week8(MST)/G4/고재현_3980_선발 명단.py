def backtracking(k, sum1):
    global max1
    if k == 11:
        max1 = max(sum1, max1)
    for i in range(11):
        if not visit[i]:
            if arr[k][i] == 0:
                continue
            visit[i] = True
            sum1 += arr[k][i]
            backtracking(k+1,sum1)
            visit[i] = False
            sum1 -= arr[k][i]


T = int(input())
for _ in range(T):
    arr = [list(map(int,input().split())) for _ in range(11)]
    visit = [False] * 11
    max1 = -1
    backtracking(0,0)
    print(max1)