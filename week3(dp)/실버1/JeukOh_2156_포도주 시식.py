import sys

n = int(input())
p = list(map(int, sys.stdin.read().split()))

if n == 1:
    print(p[0])
else:
    dp = [0]*(n+1)

    # 1번 걍 마셔
    dp[1] = p[0]
    # 2번도 걍 마셔
    dp[2] = p[0] + p[1]

    for idx in range(3,n+1):
        # 3번 이상 부터
        # 이번 포도주 잔에서,
        # 1. 먹지말던가, (저번거 마셔서 이번거 안마신게 더 이득일 수 있음)
        # 2. 3번째 전꺼부터 한번 쉬고 전 것과 이번 것 마신것과, (2잔째)
        # 3. 2번째 전꺼부터 (한턴쉬고) 이번거 먹은 것 비교 (1잔째)
        dp[idx] = max(dp[idx-1], dp[idx-3]+p[idx-2]+p[idx-1], dp[idx-2]+p[idx-1])

    print(dp[-1])
