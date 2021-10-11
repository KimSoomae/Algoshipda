#미완성 코드

input = open('input.txt').readline

N = int(input())
choo_weight = list(map(int, input().split()))
max_weight = sum(choo_weight)

dp = [[] for _ in range(N)] 

dp_memo = [0] * (max_weight + 1)
for i in range(N):
    if i == 0:
        dp[i].append(choo_weight[0])
    
    else:
        for choo in dp[i-1]:
            dp[i].append(choo_weight[i])
            dp[i].append(choo + choo_weight[i])
            dp[i].append(abs(choo - choo_weight[i]))
        
        dp[i] = list(set(dp[i]))
    
    for index in dp[i]:
        dp_memo[index] = 1

M = int(input())
print(dp)
print(dp_memo)
Q_list = list(map(int, input().split()))
for Q in Q_list:
    if dp_memo[Q]:
        print('Y', end= ' ')
    else:
        print('N', end= ' ' )