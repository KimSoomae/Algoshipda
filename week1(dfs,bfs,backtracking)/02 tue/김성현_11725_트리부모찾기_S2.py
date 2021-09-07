import sys
sys.stdin = open('input.txt')

sys.setrecursionlimit(10**6)
N = int(input())

Parent_child = [0] * (N+1)
board = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(N-1):
    s, e = map(int, input().split())
    board[s].append(e)
    board[e].append(s)

def dfs(s):
    visited[s] = 1
    for w in board[s]:
        if visited[w] == 0:
            dfs(w)
            Parent_child[w] = s

dfs(1)
for i in range(2, N+1):
    print(Parent_child[i])


