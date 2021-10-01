# 꼭 이분탐색을 안써도 되는 문제

import sys; readline = sys.stdin.readline
import math
N, M = map(int,readline().split())

anw = float('inf')
for _ in range(M):
    u, d = map(int,readline().split())
    m_min = math.ceil((d*N)/(u+d))
    height = (u*m_min-d*(N-m_min))
    if height == 0:
        height = (u*(m_min+1)-d*(N-m_min-1))
    anw = min(anw,height)

print(anw)