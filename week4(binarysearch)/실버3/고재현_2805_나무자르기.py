# sys 쓰고 pypy로 풀어야 시간초과 안남
# python3로 풀고 싶으면 sys랑
# collections import Counter 를 써야함
# 시간 초과 때문에 까다로운 문제네-_-
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)
result = 0
while start <= end:
    mid = (start + end) // 2

    sangun = 0
    for i in range(n):
        if tree[i] > mid:
            sangun += tree[i] - mid

    if sangun < m:
        end = mid - 1
    elif sangun >= m:
        result = mid
        start = mid + 1
print(result)
