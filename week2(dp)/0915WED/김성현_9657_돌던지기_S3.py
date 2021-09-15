N = int(input())
dp = [0, 'Win', 'Lose', 'Win', 'Win'] + [0]*(N-4) #['Win', 'Win', 'Lose'... ] 
# dp의 의미: 내가 시작할 때 그 자리에 있으면 패배 -> 5번째부터는 1, 3, 4개의 돌을 집어서 Lose로 보낼 수 있으면 Win, 그럴 수 없으면 Lose

if N <= 4:
    pass
else:
    for i in range(5, N+1):
        if 'Lose' in [dp[i-1], dp[i-3], dp[i-4]]:
            dp[i] = 'Win'
        else:
            dp[i] = 'Lose'
if dp[N] == 'Win':
    print('SK')
else:
    print('CY')

