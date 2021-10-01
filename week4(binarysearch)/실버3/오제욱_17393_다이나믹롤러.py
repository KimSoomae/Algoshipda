from bisect import bisect_right
import sys; readline = sys.stdin.readline

N = int(input())
ink = list(map(int,readline().split()))
jum = list(map(int,readline().split()))
anw = [0]*N
for idx in range(N):
   anw[idx] = (bisect_right(jum,ink[idx])-1-idx)
print(' '.join(str(x) for x in anw))


import sys; readline = sys.stdin.readline

N = int(input())
ink = list(map(int,readline().split()))
jum = list(map(int,readline().split()))
anw = [0]*N

for idx in range(N):
    s, e = 0, N
    ret = idx
    ik = ink[idx]
    while s < e:
        mid = (s+e)//2
        if ik < jum[mid]:
            e = mid
        else:
            s = mid+1

    anw[idx] = s-idx-1

print(' '.join(str(x) for x in anw))