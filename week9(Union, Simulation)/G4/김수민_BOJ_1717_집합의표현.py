# BOJ 1717 집합의 표현 - 유니온파인드 골드 4 김수만
# x를 포함하는 집합 찾기
def find_set(x):
    while x != P[x]:
        x = P[x]
    return x
# x와 y 포함하는 두 집합 통합
def union(x, y):
    root_x, root_y = find_set(x), find_set(y)
    P[max(root_x, root_y)] = min(root_y, root_x)

N, M = map(int, input().split())
P = [0] * (N + 1)
# 처음엔 자기 자신 가리키게
for i in range(N + 1):
    P[i] = i
for i in range(M):
    cal, a, b = map(int, input().split())
    # a와 b가 같은 경우는 연산 패스해야 시간초과 안남
    if cal == 0:
        if a != b:
            union(a, b)
    else:
        if a == b:
            print("YES")
        elif find_set(a) == find_set(b):
            print("YES")
        else:
            print("NO")