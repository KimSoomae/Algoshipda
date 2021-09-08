import sys; readline = sys.stdin.readline
from itertools import combinations

N, M = map(int,readline().split())
H = list(map(int,readline().split()))

def isPrime(s):
    flag = True
    for x in range(2, int(s**(1/2))+1):
        if not s%x:
            flag = False
            break
    return flag
anw = set()
for x in combinations(H,M):
    s = sum(x)
    if isPrime(s):
        anw.add(s)

if not anw:
    print(-1)
else:
    anw = sorted(list(anw))
    print(*anw)