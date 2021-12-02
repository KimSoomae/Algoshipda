import sys
from collections import deque
sys.setrecursionlimit(10**7)

input = open('input.txt').readline
N, V = map(int, input().split())
board = [[0]*(N+1) for _ in range(N+1)]
node_value = [0] + list(map(int, input().split()))


def dfs(s, day):
    global value, answer, endposition

    if sum(visited) == N+1:
        if answer > value:
            answer = value
            endposition = s 
            return

    for i in range(N+1):
        if board[s][i] and not visited[i]:

            value += ( 1 + node_value[i] * day)
            visited[i] = 1

            dfs(i, day+1)

            value -= ( 1 + node_value[i] * day)
            visited[i] = 0
    
for _ in range(N+1):
    info = list(map(int, input().split()))
    for j in range(1, len(info)):
        board[info[0]][info[j]] = 1

def bfs(endposition):

    Q = deque()
    Q.append(endposition)
    day = 0

    while Q:
        temp = []

        while Q:
            s = Q.pop()
            for i in range(N+1):
                if board[s][i] == 1:
                    temp.append(i)
        if 0 in temp:
            return day + 1
        
        day += 1

        for node in temp:
            Q.append(node)

visited = [1] + [0] * (N)

answer = 0xffffff
value = 0
endposition = 0
dfs(0, 1)
print(answer, endposition)
visited = [0] * (N+1)
returnday = bfs(endposition)
print(answer + returnday)
