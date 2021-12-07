input = open('input.txt').readline
from collections import deque
def bfs(i):
    q = deque()
    q.append(i)
    visit = [0 for i in range(f)]
    visit[i] = 1
    while q:
        x = q.popleft()
        for i in range(2):
            nx = x + dire[i]
            if 0 <= nx < f and visit[nx] == 0:
                q.append(nx)
                s_[nx] = s_[x] + 1
                visit[nx] = 1
f, s, g, u, d = map(int, input().split())
s_ = [-1 for i in range(f)]
dire = [u, -d]
s_[s - 1] = 0
bfs(s - 1)
print(s_[g - 1] if s_[g - 1] != -1 else "use the stairs")