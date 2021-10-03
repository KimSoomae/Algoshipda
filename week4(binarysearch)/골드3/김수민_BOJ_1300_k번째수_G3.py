# 1300 k번째 수
N = int(input())
K = int(input())
L, R = 1, K
while L <= R:
    mid = (L + R) // 2
    tmp = 0
    # tmp는 mid보다 작은애들 개수(즉, tmp의 순서)
    for i in range(1, N + 1):
        # i * j 중에서 mid보다 작은 애들 개수는 mid를 행으로 나눈 몫, N은 넘어가면 안되니까 N 넘어가면 N으로
        tmp += min(mid//i, N)
    # 구해야되는 순서가 더 앞에 있으면
    if tmp >= K:
        anw = mid
        R = mid - 1
    else:
        L = mid + 1
print(anw)