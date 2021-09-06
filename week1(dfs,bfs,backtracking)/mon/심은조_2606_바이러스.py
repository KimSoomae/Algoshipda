computer = int(input())
edge = int(input())
graph = [[] for i in range(computer+1)]
for i in range(edge):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)

dfs_visited = [0] * (computer+1)

cnt = -1

def solution1_dfs(start):
    dfs_visited[start] = True
    global cnt
    cnt += 1
    for i in graph[start]:
        if not dfs_visited[i]:
            solution1_dfs(i)

solution1_dfs(1)
print(cnt)
