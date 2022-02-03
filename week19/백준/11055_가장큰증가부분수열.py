input = open('input.txt').readline
n = int(input())
array = list(map(int, input().split()))

dp = [0 for i in range(n)]
dp[0] = array[0]

for i in range(1, n):
    s = []
    for j in range(i-1, -1, -1):
        if array[i] > array[j]:
            s.append(dp[j])
    if not s:
        dp[i] = array[i]
    else:
        dp[i] = array[i] + max(s)

            
print(max(dp))