import sys
from collections import deque
sys.setrecursionlimit(10**7)

input = open('input.txt').readline
N, V = map(int, input().split())
board = [[0]*(N+1) for _ in range(N+1)]
node_value = [0] + list(map(int, input().split()))


def dfs(s, day):

    global value, answer

    if sum(visited) == N+1:
        if answer > value+backcost[s]:
            answer = value+backcost[s]
            return

    for i in range(N+1):
        if board[s][i] and not visited[i]:

            value += ( 1 + node_value[i] * day)
            visited[i] = 1
            if value < answer:
                dfs(i, day+1)

            value -= ( 1 + node_value[i] * day)
            visited[i] = 0
    
for _ in range(N+1):
    info = list(map(int, input().split()))
    for j in range(1, len(info)):
        board[info[0]][info[j]] = 1

def make_back_cost():
    backcost[0] = 0
    visited = [1] + [0]*(N)
    day = 1
    Q = deque()
    Q.append(0)

    while Q:

        temp = []

        while Q:
            s = Q.pop()
            for i in range(N+1):
                if board[s][i] == 1 and not visited[i]:
                    backcost[i] = day
                    visited[i] = 1
                    temp.append(i)
        
        for node in temp:
            Q.append(node)
        day += 1
        



visited = [1] + [0] * (N)
backcost = [0] * (N+1)
# i번째 노드에서 집까지 가는데 필요한 비용

answer = 0xffffff
value = 0
endposition = 0
make_back_cost()
dfs(0, 1)

print(answer)


