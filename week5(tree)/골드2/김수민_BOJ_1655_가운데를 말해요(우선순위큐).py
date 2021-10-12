# 1655 가운데를 말해요 - 우선순위 큐 골드 2 김수민
import heapq
import sys
left_h = [] # 왼쪽 최대 힙
right_h = [] # 오른쪽 최대 힙
mid = 0
N = int(sys.stdin.readline())
mid = int(sys.stdin.readline())
print(mid)
for i in range(1, N):
    n = int(sys.stdin.readline())
    if n > mid: # 중간 값보다 크면
        heapq.heappush(right_h, n) # 오른쪽 큐에 삽입
        if len(left_h) + 1 < len(right_h): # 오른쪽 큐가 원소 2개이상 더 많으면
            heapq.heappush(left_h, (-mid, mid)) # 최소 값 업데이트
            mid = heapq.heappop(right_h)
    else: # 중간 값보다 작으면
        heapq.heappush(left_h, (-n, n)) # 왼쪽 큐에 삽입
        if len(right_h) < len(left_h): # 왼쪽 큐가 원소 1개 이상 더 많으면(중간값 2개일 때 더 작은 값이 mid이므로)
            heapq.heappush(right_h, mid) # 중간 값 업데이트
            mid = heapq.heappop(left_h)[1]
    print(mid)

