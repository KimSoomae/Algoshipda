import sys

# sys.stdin = open('김병완_14889_스타트와_링크.txt', 'r')

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dfs(step):
    global mini
    if len(A) == N >> 1:
        totalA = totalB = 0
        tmp_B = []
        for player in all:
            if player not in A:
                tmp_B.append(player)
        for i in range(N >> 1):
            for j in range(N >> 1):
                totalA += S[A[i] - 1][A[j] - 1]
                totalB += S[tmp_B[i] - 1][tmp_B[j] - 1]
        if abs(totalA - totalB) < mini:
            mini = abs(totalA - totalB)
        return
    elif len(B) == N >> 1:
        totalA = totalB = 0
        tmp_A =[]
        for player in all:
            if player not in B:
                tmp_A.append(player)
        for i in range(N >> 1):
            for j in range(N >> 1):
                totalB += S[B[i] - 1][B[j] - 1]
                totalA += S[tmp_A[i] - 1][tmp_A[j] - 1]
        if abs(totalA - totalB) < mini:
            mini = abs(totalA - totalB)
        return
    else:
        for i in range(2):
            if i:
                A.append(step)
                dfs(step + 1)
                A.pop()
            else:
                B.append(step)
                dfs(step + 1)
                B.pop()
A = []
B = []
all = list(range(1, N + 1))
mini = 99 * N
dfs(1)
print(mini)