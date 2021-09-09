import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

N = int(input())

start, end = map(int, input().split())

L = int(input())

board = [[0] * (N+1) for _ in range( N+1 )]
visited = [0] * (N+1)

for i in range(L):
    s, e = map(int, input().split())
    board[s][e] = 1
    board[e][s] = 1


def dfs(s):
    global cnt
    global is_valid
    visited[s] = 1
    for i in range(1, N+1):
        if not visited[i] and board[s][i] == 1:
            cnt += 1
            if i == end:
                print(cnt)
                is_valid = 1
                return
            else:
                dfs(i)
            cnt -= 1
            
cnt = 0
is_valid = 0 
dfs(start)
if is_valid == 0:
    print(-1)
