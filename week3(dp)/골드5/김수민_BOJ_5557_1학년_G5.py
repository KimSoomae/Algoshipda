# 백준 5557 1학년 - dp G5 김수민
anw = 0
def dfs(cnt, sum):
    global anw
    # 음수거나 20 넘어가면 리턴
    if sum < 0 or sum > 20:
        return 0
    # 연산 끝났을때(마지막 =을 앞두고)
    if cnt == N - 2:
        # == 마지막숫자면
        if sum == num[N-1]:
            # 1가지 경우 가능함을 저장하고 리턴
            dp[cnt][sum] = 1
            return dp[cnt][sum]
        # != 마지막 숫자면 이미 구해봤는데 가능하지 않음을 나타내기 위해 0을 저장하고 리턴
        dp[cnt][sum] = 0
        return dp[cnt][sum]
    # 이미 0이나 1로 업뎃된거면 계산 안해봐도 되니까 저장된 값을 리턴
    if dp[cnt][sum] != -1:
        return dp[cnt][sum]
    anw = 0
    # 덧셈
    anw += dfs(cnt + 1, sum + num[cnt + 1])
    # 뺄셈
    anw += dfs(cnt + 1, sum - num[cnt + 1])
    # 업뎃된 anw 저장(dp[7][0]=2 이면 7번째에 sum이 0일 때 그 이후에 연산으로 올바른 등식이 되는 경우의 수가 2개인 것
    dp[cnt][sum] = anw
    return dp[cnt][sum]

N = int(input())
num = list(map(int, input().split()))
# dp[cnt][sum] cnt번 째에 계산값이 sum이면 마지막 숫자로 연산하는데 몇번이 걸리는지 저장하는 배열
dp = [[-1] * 25 for _ in range(101)]
print(dfs(0, num[0]))