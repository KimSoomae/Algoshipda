# 2805 나무자르기 - 이분탐색 S3 김수민
N, M = map(int, input().split())
arr = list(map(int, input().split()))
# L, R은 절단기에 설정할 높이의 최소값, 최대값
L = 0
R = max(arr)
anw = 0
while L <= R:
    mid = (L + R) // 2
    tree = 0
    for i in range(N):
        if (arr[i] > mid):
            # 절단기에 잘리는 나무들
            tree += (arr[i] - mid)
    # 잘린 나무들이 집에 가져가야될 나무보다 길면 절단기 높이 높여준다
    if tree >= M:
        anw = mid
        L = mid + 1
    # 짧으면 절단기 높이 낮춰준다
    else:
        R = mid - 1
print(anw)