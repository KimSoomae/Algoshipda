import sys
sys.stdin = open('input.txt')

'''input
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
'''


sys.setrecursionlimit(10**6)
C, R = map(int, input().split())

board = [[0] * (R+1)]
for i in range(C):
    column = [0] + list(map(int, input().split()))
    board.append(column)

# case input에 대해서
# f(c, r) = board[c][r]에 대한 판별
# f(1,1) = f(2,1) + f(1,2)
# 상하좌우 4방향에 대해서 유효한 지점(1~c/1~r index안에 있을 것, 현재 value에 비해서 도착지점의 value가 낮을 것)

# start = f(1,1) end = f(c, r)
# 해당 칸의 value : board[c][r]


# 1. dfs - 시간초과
'''
dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]
cnt = 0
def dfs(c, r):
    global cnt
    if c == C and r == R:
        cnt +=1
    else:
        for i in range(4):
            new_c = c + dc[i]
            new_r = r + dr[i]
            if 1 <= new_c <= C and 1 <= new_r <= R:
                if board[new_c][new_r] < board[c][r]:
                    dfs(new_c, new_r)

dfs(1, 1)
print(cnt)      
'''

# 2. dp
'''input
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
'''

''' dp value initial
0 1 1 1 1
1 0 0 2 1
1 0 0 2 0
1 1 1 3 3

뒤집어서 f(1,1) 기준으로 변환하면
3 2 2 2 1
1 0 0 1 1
1 0 0 1 1
1 1 1 1 1

'''


#dp (1,1)에서 시작 - dp(C, R)에서 마무리
#dp (1,1) = 4방향 중 유효한 좌표-[해당 value가 현재 value보다 낮을 것]에 대해서 dp(a, b)를 더하면 됨

#생각해보니 append방식이 아닌 수정 방식이기 때문에 시작점을 종료지점으로 설정해야 할듯 싶다.

dp_memo = [[0]* (R+1) for _ in range(C+1)] #메모이제이션할 dp
dp_memo[C][R] = 1 

dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]
def dp(c, r):
    global dp_memo
    for i in range(4): #4방향 검사
        new_c = c + dc[i] 
        new_r = r + dr[i]
        if 1 <= new_c <= C and 1 <= new_r <= R:
            if board[new_c][new_r] > board[c][r]: #유효한 좌표의 value > 현재 좌표의 value
                dp_memo[new_c][new_r] += 1
                dp(new_c, new_r)


dp(C, R)
print(dp_memo[1][1])





