# 포도주 시식 김수민
# n이 3보다 작을 때 처리를 잘 해주기!!! 안먹고 넘어가는 경우를 생각 못해서 오래 걸림..
n = int(input())
wine = []
for i in range(n):
    wine.append(int(input()))
dp = [wine[0]] + [0] * n
if n == 2:
    dp[1] = wine[0] + wine[1]
elif n >= 3:
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0]+wine[2], wine[1]+wine[2], dp[1])
    # 3번 연속 마시면 안되니까 가능한 경우는 아래 세가지 경우 밖에 없음
    # 전전 최대값 + 지금 마시기, 전전전최대갑 + 전포도주 + 지금 마시기, 전최대값 + 지금 안마시기 중 최대값
    for i in range(3, n):
        dp[i] = max(dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i], dp[i-1])
print(dp[n-1])
