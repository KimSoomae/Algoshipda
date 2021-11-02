# BOJ 1446 지름길 - 다익스트라 실버1 김수민
from collections import defaultdict
N, D = map(int, input().split())
short_way = defaultdict(list) # 지름길 저장할 리스트 딕셔너리
for i in range(N):
    s, e, d = map(int, input().split())
    short_way[s].append((e,d))
dis = []
# 거리는 최대 지름길 없이 가는 것만큼이므로 좌표값 저장
for i in range(D + 1):
    dis.append(i)
for i in range(D + 1):
    # 원래 값보다 전에 위치 + 1로 가는게 빠르면 업데이트
    if i >= 1: dis[i] = min(dis[i], dis[i-1] + 1)
    # 현재 위치에서 지름길 있으면
    if len(short_way[i]) > 0:
        while (short_way[i]):
            e, d = short_way[i].pop()
            # 도착지점이 최종도착점보다 작거나 같고, 지름길로 가는게 원래 도착지점의 거리에 저장된 갑보다 작으면
            if e <= D and dis[i] + d < dis[e]:
                dis[e] = dis[i] + d
print(dis[D])