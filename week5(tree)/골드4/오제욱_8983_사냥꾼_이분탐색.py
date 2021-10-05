import sys; readline = sys.stdin.readline
from bisect import bisect
M, N, L = map(int,readline().split())
guns = list(map(int,readline().split()))
animals = []
for _ in range(N):
    x,y = map(int,readline().split())
    if y <= L:
        animals.append((x,y))

guns.sort()
cnt = 0
for ani in animals:
    ani_x = bisect(guns,ani[0])
    if M > ani_x >= 1:
        k = ani[1]+min(abs(guns[ani_x]-ani[0]),abs(guns[ani_x-1]-ani[0]))
    elif ani_x == M:
        k = ani[1]+abs(guns[ani_x-1]-ani[0])
    else:
        k = ani[1]+abs(guns[ani_x]-ani[0])
    if k <= L:
        cnt += 1

print(cnt)