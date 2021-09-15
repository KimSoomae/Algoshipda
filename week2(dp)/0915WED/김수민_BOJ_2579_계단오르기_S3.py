N = int(input())
step = [] # 계단 점수 저장할 리스트
dp = [0] * 302 # 밟는 계단 별로 최대 점수 저장할 리스트
for i in range(N):
    step.append(int(input()))
# N = 1, 2, 3일때는 채워 놓기
dp[0] = step[0]
if N == 2:
    dp[1] = step[0] + step[1]
elif N >= 3:
    dp[1] = step[0] + step[1]
    dp[2] = max(step[1] + step[2], dp[0] + step[2])
    for i in range(3, N):
        # 마지막 N번째 계단 꼭 밟아야되니까 전계단 밟는 경우, 전전계단 밟아서 점프하는 경우 중 max 값
        dp[i] = max(dp[i-3]+step[i-1]+step[i], dp[i-2]+step[i])
print(dp[N-1])
