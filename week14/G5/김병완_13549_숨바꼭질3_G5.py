import sys; sys.stdin = open('13549_숨바꼭질3_G5.txt', 'r')
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
fields = [-1] * 100001
check = [False] * 100001

fields[N] = 0
check[N] = True

q = deque()
q.append(N)

while q:
    posi = q.popleft()
    if posi * 2 < 100001 and (not check[posi * 2]):
        q.appendleft(posi * 2)
        check[posi * 2] = True
        fields[posi * 2] = fields[posi]
    if posi + 1 < 100001 and (not check[posi + 1]):
        q.append(posi + 1)
        check[posi + 1] = True
        fields[posi + 1] = fields[posi] + 1
    if posi - 1 >= 0 and (not check[posi - 1]):
        q.append(posi - 1)
        check[posi - 1] = True
        fields[posi - 1] = fields[posi] + 1

print(fields[K])
