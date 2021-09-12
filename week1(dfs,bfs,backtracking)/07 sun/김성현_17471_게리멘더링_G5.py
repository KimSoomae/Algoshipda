import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

N = int(input())
arr = list(map(int, input().split()))
total_pop = sum(arr)
board = [[0]*(N+1) for _ in range(N+1)]
min_value = 10**3
n = len(arr)



for u in range(1, N+1):
    info = list(map(int, input().split()))
    for v in range(1, info[0]+1):
        board[u][info[v]] = 1
        board[info[v]][u] = 1

def dfs(u, lst, visited):
    for v in lst:
        if board[u][v] == 1 and not visited[v]:
            visited[v] = 1
            dfs(v, lst, visited)

def is_valid(lst):
    cnt = 0
    visited = [0] * (N+1)
    for u in lst:
        if visited[u] == 0:
            cnt += 1
            dfs(u, lst, visited)

    if cnt > 1 or cnt == 0:    
        return False
    
    return True

is_exist = False
for i in range(1<<n):
    temp = []
    group_A = []

    for j in range(n+1):
        if i & (1<<j):
            temp.append(arr[j])
            group_A.append(j+1)
    group_B = list(range(1, N+1))
    for x in group_A:
        group_B.remove(x)

    if is_valid(group_A) and is_valid(group_B):
        is_exist = True
        sum_group_A = 0
        for y in group_A:
            sum_group_A += arr[y-1]
        
        sum_group_B = total_pop - sum_group_A
        min_value = min(min_value, abs(sum_group_B-sum_group_A))

if is_exist == False:
    print(-1)
else:
    print(min_value)
    # 선거구의 구역수 > 0
    # 선거구는 반드시 이어지는 구간이 있어야함
