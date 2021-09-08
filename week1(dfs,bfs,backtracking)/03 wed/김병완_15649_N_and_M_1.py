import sys

N, M = map(int, sys.stdin.readline().split())

def DFS():
    if len(s) == M:
        print(*s)
        return
    for i in range(1, N + 1):
        if visited[i]:
            continue

        visited[i] = 1
        s.append(i)
        DFS()
        s.pop()
        visited[i] = 0

s = []
visited = [0] * (N + 1)
DFS()


