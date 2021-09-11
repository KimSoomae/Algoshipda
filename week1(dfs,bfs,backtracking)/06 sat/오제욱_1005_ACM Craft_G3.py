import sys; readline = sys.stdin.readline

for _ in range(int(readline().rstrip())):
    N, K = map(int,readline().split())
    build_time = [-1]+list(map(int,readline().split()))
    root = [[] for i in range(N+1)]

    for _ in range(K):
        a, b = map(int,readline().split())
        root[b].append(a)

    fin = int(readline().rstrip())
    dp = [-1]*(N+1)
    def recur(node):
        if dp[node] != -1:
            return dp[node]
        time = 0
        for x in root[node]:
            tmp = recur(x)
            time = max(time,tmp)
        dp[node] = time + build_time[node]
        return dp[node]
    recur(fin)
    if dp[fin] == -1:
        print(build_time[fin])
    else:
        print(dp[fin])



