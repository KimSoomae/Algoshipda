import sys; read = sys.stdin.readline
import heapq
N, K = map(int,read().split())
alls = []
for _ in range(N):
    M, V = map(int,read().split())
    alls.append([M,V])

for _ in range(K):
    K = int(read().strip())
    # -1 안댐, 제일 큰 값을 해야 무게가 같은 보석과 가방 중
    # 가치를 기준으로 가방이 제일 뒤로 줄을 선다.
    #alls.append([K,-1])
    alls.append([K, 10**6+1])

# 무게를 기준으로 정렬하고 가방의 경우 가치를 구분하여 가방임을 표시

alls.sort()
anw = 0
buffer = []

print(alls)

# 무게가 낮은 거 부터 -> 가방을 만나면 무조건 넣을 수 있다.
for x in alls:
    # 보석이라면
    if x[1] != 10**6+1:
        # 가치가 큰 것이 우선적으로 오게 힙 삽입 buffer는
        # 넣을 수 있는 후보 보석들을 담음
        heapq.heappush(buffer,-x[1])
    #가방이라면
    else:
        # 후보 보석들 중 가장 가치가 큰 놈을 빼서 가방에 넣는다.
        if buffer:
            anw += -heapq.heappop(buffer)

print(anw)

# 버퍼로 힙을 쓰기 -> 가방과 보석을 합쳐서 줄세우기
# 어렵다!

# 이분탐색을 활용해보려고 한 시간초과

# jewels = []
# for _ in range(N):
#     M, V = map(int,read().split())
#     heapq.heappush(jewels,(-V,M))
#
# bags = [int(read().strip()) for _ in range(K)]
# bags.sort()
# # print(jewels)
# # print(bags)
# onoff = [True]*K
# poss_len = K
# anw = 0
# while jewels and poss_len:
#     jewel = heapq.heappop(jewels)
#     V, M = -jewel[0], jewel[1]
#
#     idx = bisect.bisect_left(bags,M)
#     while idx < K and not onoff[idx]:
#         idx += 1
#
#     if idx >= K:
#         continue
#
#     poss_len -= 1
#     anw += V
#     onoff[idx] = False
#
# print(anw)