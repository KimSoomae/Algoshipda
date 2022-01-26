import sys; sys.stdin = open('1149_RGB거리_S1.txt', 'r')
input = sys.stdin.readline

N = int(input())

rgb_nums = [list(map(int, input().split())) for _ in range(N)]
r1, g1, b1 = rgb_nums[0]
dp = [[r1, g1, b1]]
for i in range(1, N):
    r, g, b = dp[-1]
    nr = rgb_nums[i][0] + min(g, b)
    ng = rgb_nums[i][1] + min(r, b)
    nb = rgb_nums[i][2] + min(r, g)
    dp.append([nr, ng, nb])

print(min(dp[-1]))