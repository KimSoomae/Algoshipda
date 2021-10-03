import sys; readline = sys.stdin.readline
anw = []
for _ in range(int(input())):
    N, K = map(int,readline().split())
    arr = list(map(int,readline().split()))
    arr.sort()
    min_inteval = float('inf')
    cnt = 0
    s = 0
    e = N-1
    while s < e:
        tmp = arr[s] + arr[e]
        if abs(K-tmp) < min_inteval:
            min_inteval = abs(K-tmp)
            cnt = 1
        elif abs(K-tmp) == min_inteval:
            cnt += 1
        if tmp > K:
            e -= 1
        elif tmp == K:
            e -= 1
            s += 1
        else:
            s += 1
    anw.append(cnt)

print('\n'.join(str(x) for x in anw))