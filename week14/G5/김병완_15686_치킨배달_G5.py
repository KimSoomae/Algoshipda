import sys; sys.stdin = open('15686_치킨배달_G5.txt', 'r')
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

stores = []
houses = []
dis = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 2:
            stores.append((i, j))
        elif tmp[j] == 1:
            houses.append((i, j))


comb = combinations(stores, M)

for com in comb:
    tmp_total = 0
    for house in houses:
        tmp = 0xffffff
        for can in com:
            tmp = min(tmp, abs(can[0] - house[0]) + abs(can[1] - house[1]))
        tmp_total += tmp
    dis.append(tmp_total)

print(min(dis))


