import sys
sys.stdin = open('김병완_1943_동전분배_G3.txt', 'r')
# import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

for tc in range(3):
    # 동전 종류의 갯수
    N = int(input())
    coin_info = {}
    total = 0
    # dp = [0] * 75001 # 10만원 넘지 않으니까 나누면 딱
    # dp[0] = 1 # 0원부터 시작하니까 0원 체킹
    for i in range(N):
        coin, num = map(int, input().split())
        coin_info[coin] = num
        total += coin * num
    if total % 2:
        print(0)
        continue
    quot = total >> 1
    dp = [0] * (quot + 1)   # 우리 관심은 딱 quot까지만이잖아
    dp[0] = 1  # 0원부터 시작하니까 0원 체킹
    # 이렇게 하면 계속 첫번쨰 배수 단위로 checking함
    # for coin in coin_info:
    #     for val in range(50001):
    #         if dp[val]:
    #             for cnt in range(coin_info[coin] + 1):
    #                 dp[val + coin * cnt] = 1
    # 뒤에서 부터 긁으면 해결?
    for coin in coin_info:
        if quot < coin: continue
        for val in range(quot, -1, -1):
            if dp[val]:
                for cnt in range(coin_info[coin] + 1):
                    if val + coin * cnt > quot: continue
                    dp[val + coin * cnt] = 1
    print(dp[quot])

