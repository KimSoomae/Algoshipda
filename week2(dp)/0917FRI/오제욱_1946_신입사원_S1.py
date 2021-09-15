import sys; readline = sys.stdin.readline
for _ in range(int(input())):
    N = int(readline().rstrip())
    x = [0]*(N+1)
    for __ in range(N):
        a, b = map(int,readline().split())
        x[a] = b
    cnt = 1
    maxv = x[1]
    for idx in range(2,len(x)):
        if maxv > x[idx]:
            cnt += 1
            maxv = x[idx]
    print(cnt)

# 2632ms


# import sys; readline = sys.stdin.readline
# for _ in range(int(input())):
#     N = int(readline().rstrip())
#     x = [list(map(int,readline().split())) for __ in range(N)]
#     x.sort()
#     dp = [1]*len(x)
#     maxv = x[0][1]
#     for idx in range(len(x)-1):
#         if maxv > x[idx+1][1]:
#             dp[idx+1] = dp[idx] + 1
#             maxv = x[idx+1][1]
#         else:
#             dp[idx+1] = dp[idx]
#     print(dp[-1])

# 6304ms