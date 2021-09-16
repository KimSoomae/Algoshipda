N = int(input())
arr = list(map(int, input().split()))
# dp: 처음부터 현재 인덱스까지 최대 부분수열 길이 저장, 첫번째 값은 1(자기 포함)
dp = [1] + [0] * N
for i in range(1, N):
    tmp = 0
    # 자기보다 앞에 있는 애들 중에
    for j in range(0, i):
        # 자기보다 작으면서 dp는 최대값인 애 찾아서
        if arr[j] < arr[i] and dp[j] > tmp:
            tmp = dp[j]
    # 길이 + 1 (부분수열에 추가)
    dp[i] = tmp + 1
print(max(dp))