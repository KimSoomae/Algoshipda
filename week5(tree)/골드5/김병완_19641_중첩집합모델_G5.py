import sys; sys.stdin = open('김병완_19641_중첩집합모델_G5.txt', 'r')
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

# def dfs(n, parent):
#     global cnt
#     if sum(info[n]) - 1 == 0:
#         result[n - 1][0] = cnt
#         result[n - 1][1] = cnt + 1
#         cnt += 2
#     else:
#         result[n - 1][0] = cnt
#         cnt += 1
#         for idx in range(1, N + 1):
#             if idx == parent: continue
#             if info[n][idx]:
#                 dfs(idx, n)
#         result[n - 1][1] = cnt
#         cnt += 1

def dfs(n, parent):
    global cnt
    result[n - 1][0] = cnt
    cnt += 1
    for idx in info[n]:
        if idx == parent: continue
        dfs(idx, n)
    result[n - 1][1] = cnt
    cnt += 1

N = int(input())
info = {}
for _ in range(N):
    tmp = list(map(int, input().split()))
    info[tmp[0]] = []
    for i in range(1, len(tmp) - 1):
        info[tmp[0]].append(tmp[i])
    info[tmp[0]].sort()
root = int(input())
result = [[0, 0] for _ in range(N)]
cnt = 1
dfs(root, 0)
for idx, value in enumerate(result):
    print(idx + 1, ' '. join(map(str, value)))




