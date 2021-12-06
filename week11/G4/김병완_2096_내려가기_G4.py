import sys; sys.stdin = open('2096_내려가기_G4.txt', 'r')

input = sys.stdin.readline

def slide(maxi, mini, lis):
    max_visit = [False] * 3
    min_visit = [False] * 3
    tmp_max = [0] * 3
    tmp_min = [0] * 3
    for i in range(3):
        for j in range(3):
            ni = i + di[j]
            if ni < 0 or ni >= 3: continue
            if not max_visit[ni]:
                tmp_max[ni] = maxi[i] + lis[ni]
                max_visit[ni] = True
            else:
                tmp_max[ni] = max(tmp_max[ni], maxi[i] + lis[ni])
            if not min_visit[ni]:
                tmp_min[ni] = mini[i] + lis[ni]
                min_visit[ni] = True
            else:
                tmp_min[ni] = min(tmp_min[ni], mini[i] + lis[ni])
    return (tmp_max, tmp_min)

N = int(input())
di = [-1, 0, 1]
maxi = [0, 0, 0]
mini = [0, 0, 0]

for i in range(N):
    tmp_list = list(map(int, input().split()))
    maxi, mini = slide(maxi, mini, tmp_list)

print(max(maxi), min(mini))