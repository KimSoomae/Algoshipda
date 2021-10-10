import sys; readline=sys.stdin.readline
from heapq import *
N = int(readline())
a = []
for _ in range(N):
    heappush(a,int(readline()))
anw = 0
while len(a) >= 2:
    b = heappop(a)
    c = heappop(a)
    heappush(a,b+c)
    anw += (b+c)
print(anw)