input = open('input.txt').readline

N = int(input())
dp = [0] * 31
dp[0] = 1
dp[2] = 3

for i in range(4, 31):
    if not i % 2:
        sub_answer = 0
        
        k = i-2
        sub_answer += 3*dp[k]
        while k >= 0:
            k -= 2
            sub_answer += 2*dp[k]
        dp[i] = sub_answer
print(dp[N])

'''
f(0) = 1
f(2) = 3
f(N) = 3 * f(N-2) + 2 * f(N-4) + 2 * f(N-6) + ...
'''