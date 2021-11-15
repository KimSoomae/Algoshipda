from collections import deque

input = open('input.txt').readline

def bfs():
    q = deque()

    q.append(X)
    dist[X] = 0

    while q:
        d = q.popleft()
        if d == 123456789:
            return dist[d]

        s = str(d)
        k = s.find('9')
        c, r = k//3, k%3

        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]

            if 0 <= nc < 3 and 0 <= nr < 3:
                nk = nc * 3 + nr
                ns = list(s)
                ns[k], ns[nk] = ns[nk], ns[k]

                nd = int(''.join(ns))

                if not dist.get(nd):
                    dist[nd] = dist[d]+1
                    q.append(nd)
    return -1




dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]

dist = dict()

X = ''

for i in range(3):
    x = input().strip()
    x = x.replace(' ','')
    X += x

X = int(X.replace('0', '9'))
print(bfs())
    