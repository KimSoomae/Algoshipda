k, n = map(int, input().split())
lan = []
for _ in range(k):
    lan.append(int(input()))
start, end = 1, max(lan)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for l in lan:
        cnt += l // mid
    if cnt >= n: # 너무 작게 잘라서 갯수가 초과하거나 잘 잘라서 딱 떨어지지만 더 크게 자를 순 없나?
        result = mid
        start = mid + 1
    else: # 너무 크게 잘라서 갯수가 모자름
        end = mid - 1

print(result)

