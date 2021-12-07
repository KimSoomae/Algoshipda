import sys; sys.stdin = open('14502_숨바꼭질_G5.txt', 'r')
from collections import deque

input = sys.stdin.readline
field = [[-1, 0] for _ in range(100001)]
N, K = map(int, input().split())

Q = deque()
Q.append((N, 0))
field[N][0] = 0
field[N][1] = 1

while Q:
    loc, time = Q.popleft()
    for after in (loc - 1, loc + 1, loc * 2):
        if after < 0 or after >= 100001: continue
        if field[after][0] == -1:
            field[after][0] = field[loc][0] + 1
            field[after][1] = field[loc][1]
            Q.append((after, time + 1))
        elif field[after][0] == time + 1:
            field[after][1] += field[loc][1]

print(field[K][0])
print(field[K][1])

