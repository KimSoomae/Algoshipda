# 이분탐색 1920 수찾기 - 김수민
def binary_search(start, end, n):
    mid = (start + end) // 2
    # 원하는 수 찾았으면 1 리턴
    if num[mid] == n:
        return 1
    # 아직 탐색 가능하고
    if mid >= start and mid <= end:
        # 탐색 하고있는 수보다 찾아야되는 수가 작으면 왼쪽 탐색
        if num[mid] > n:
            return binary_search(start, mid -1, n)
        # 탐색 하고있는 수보다 찾아야되는 수가 크면 오른쪽 탐색
        else:
            return binary_search(mid + 1, end, n)
    else:
        return 0

N = int(input())
num = list(map(int, input().split()))
num.sort()
M = int(input())
check = list(map(int, input().split()))
for i in range(M):
    print(binary_search(0, N - 1, check[i]))