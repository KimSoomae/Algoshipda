import sys 
from pprint import pprint
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(y, x):
    visited[y][x] = 1
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        
        if 0 <= new_y <= N-1 and 0 <= new_x <= M-1:
            if board[new_y][new_x] and not visited[new_y][new_x]:
                dfs(new_y, new_x)



TC = int(input())
for case_number in range(1, TC+1):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    visited = [[1] * M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        board[y][x] = 1
        visited[y][x] = 0

    cnt = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] and not visited[y][x]:
                dfs(y, x)
                cnt += 1

    print(cnt)






'''
2 3 1 0 0 0 0 0 0 0 
2 2 1 0 1 0 0 0 0 0
0 1 0 1 2 0 0 0 0 0
0 0 1 2 2 1 0 1 1 1
0 1 2 2 3 0 1 3 4 3
0 0 0 0 1 0 1 4 5 4
0 0 0 0 0 0 1 3 4 3
0 0 0 0 0 0 0 1 1 1
'''    
