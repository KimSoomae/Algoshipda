import sys
sys.stdin = open('input.txt')

N = int(input())
jump = [0] + list(map(int, input().split()))
s = int(input())
cnt = 1
visited = [0] * (N + 1)

def dfs(s):

    global cnt
    visited[s] = 1
    jl = jump[s]
    front = s - jl
    end = s + jl
    if 1 <= front <= N and visited[front] == 0:
        cnt += 1
        dfs(front)

    if 1 <= end <= N and visited[end] == 0:
        cnt += 1
        dfs(end)

dfs(s)
print(cnt)
print(visited)