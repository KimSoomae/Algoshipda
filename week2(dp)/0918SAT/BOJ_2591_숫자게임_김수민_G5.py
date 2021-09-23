# BOJ 2591 G5 김수민
s = list(map(int, input()))
n = len(s)
dp = [0] * n
dp[0] = 1
# 13, 24 같은 경우 1,3 / 13 두가지 경우이므로 0 포함 경우 빼고 2로 세팅
if (s[1] != 0) and ((1 <= s[0] <= 2) or (s[0] == 3 and s[1] <= 4)):
    dp[1] = 2
else:
    dp[1] = 1

for i in range(2, n):
    # 0은 단독으로 숫자로 쓰일 수 없고 그 앞의 자리수와 함께 가야되므로 그 전전걸 가져옴
    # Ex) 2 1 0 이면 2 / 10 밖에 안됨
    if s[i] == 0:
        dp[i] = dp[i-2]
    # 0이 없고, 11~34에 포함되면 각 숫자 따로랑 같이 두가지 경우로 나눌 수 있음
    # Ex) 2 7 1 2 에서 7까지 두가지 경우가 있다고 하면, 마지막 2를 검사할 때 (2, 7 경우) x  2 (1, 2 / 12) + (2, 7, 1 경우 - 앞에서 카운팅 한 2, 7 경우 )
    elif ((1 <= s[i-1] <= 2) and(1 <= s[i] <= 9)) or ((s[i-1] == 3 and 1 <= s[i] <= 4)):
        dp[i] = dp[i-2] * 2 + (dp[i-1] - dp[i-2])
    # 나머지는 그 숫자 하나 세는 한가지 경우밖에 없으므로 그대로
    else:
        dp[i] = dp[i - 1]
print(dp[n-1])
