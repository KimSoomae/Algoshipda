import sys
sys.stdin = open('virus.txt', 'r')

N = int(sys.stdin.readline())
arr = [[] for _ in range(N + 1)]
for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

# S = [1]
# visit = [0] * (N + 1)
# visit[1] = 1
# start = 1
# while S:
#     for nod in arr[start]:
#         if not visit[nod]:
#             visit[nod] = 1
#             S.append(nod)
#             start = nod
#             break
#     else:
#         start = S.pop()
#
visit = [0] * (N + 1)
cnt = -1
def go_step(n):
    visit[n] = 1
    global cnt
    cnt += 1
    for candidate in arr[n]:
        if not visit[candidate]:
            go_step(candidate)

go_step(1)
print(cnt)

