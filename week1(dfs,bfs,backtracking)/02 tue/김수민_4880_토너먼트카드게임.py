def game(s, e):
    if s == e:
        return a[s]
    else:
        mid = (s + e ) // 2
        lmax = game(s, mid)
        rmax = game(mid+1, e)
        if lmax[0] == 1:
            if rmax[0] == 1:
                return lmax
            elif rmax[0] == 2:
                return rmax
            else:
                return lmax
        elif lmax[0] == 2:
            if rmax[0] == 1:
                return lmax
            elif rmax[0] == 2:
                return lmax
            else:
                return rmax
        else:
            if rmax[0] == 1:
                return rmax
            elif rmax[0] == 2:
                return lmax
            else:
                return lmax

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    a = [[0] * 2 for _ in range(N)]
    for i in range(0, N):
        a[i][0] = arr[i]
        a[i][1] = i + 1
    anw = game(0, len(arr)-1)[1]
    print(f'#{tc} {anw}')