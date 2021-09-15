l = list(map(int,input().rstrip()))
dp = [0]*(len(l)+1)
dp[0] = 1
dp[1] = 1
for idx in range(2,len(l)+1):
    if l[idx-1]:
        dp[idx] += dp[idx-1]
    if l[idx-2] and l[idx-2]*10 + l[idx-1] <= 34:
        dp[idx] += dp[idx-2]
print(dp[-1])

'''
반례 조심
항상 OJ의 예제말고도 케이스 분류해서 생각해보기 ㅜ
0 조심
3012 -> 2
30 -> 1
123456 -> 5
'''