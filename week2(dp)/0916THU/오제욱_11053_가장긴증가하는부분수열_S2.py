from bisect import bisect_left
import sys; readline = sys.stdin.readline

N = int(input())
v = list(map(int,readline().split()))
LIS = [v[0]]
for idx, va in enumerate(v):
    if not idx:
        continue
    if va > LIS[-1]:
        LIS.append(va)
    else:
        x = bisect_left(LIS,va)
        LIS[x] = va
print(len(LIS))