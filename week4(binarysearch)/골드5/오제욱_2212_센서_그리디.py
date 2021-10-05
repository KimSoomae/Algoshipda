import sys; readline = sys.stdin.readline
N = int(input())
K = int(input())
censors = list(map(int,readline().split()))
censors.sort()
anw = censors[-1]-censors[0]
dif = [0]*(N-1)
for idx in range(N-1):
    dif[idx] = censors[idx+1]-censors[idx]
dif.sort()
for _ in range(K-1):
    try:
        anw -= dif.pop()
    except:
        pass
print(anw)