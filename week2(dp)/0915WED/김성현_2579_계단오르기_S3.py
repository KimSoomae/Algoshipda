import sys
sys.stdin = open('input.txt')

N = int(input())
stair_value = [0] + [int(input()) for _ in range(N)]


max_score = [0] * (N+1)
if len(stair_value) > 2:
    for i in range(len(stair_value)):
        max_score[1] = stair_value[1]
        max_score[2] = stair_value[1] + stair_value[2]
else:
    print(stair_value[1])

def stair(n):
    global max_score
    if n < 3:
        return max_score[n]
    else:
        for i in range(3, n+1):
            max_score[i] = (max(max_score[i-2], max_score[i-3] + stair_value[i-1])+stair_value[i])
        return max_score[n]
    
if N > 1:
    print(stair(N))