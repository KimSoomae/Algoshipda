n = int(input())
arr = list(map(int,input().split()))
dp = [0] * n
dp[0] = 1

for i in range(1,n):
    max_val = 0
    for j in range(0,i):
        if arr[i] > arr[j]:
            max_val = max(max_val,dp[j])
    dp[i] = max_val + 1
    print(dp)

print(max(dp))

# 나보다 왼쪽에 있고 나보다 작은 애들 중, 가장 긴 수열(dp[i])을 가진 애를 골라 +1을 해준다.