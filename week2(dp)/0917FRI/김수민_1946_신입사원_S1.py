# PyPy로 하면 통과되는데 Python으로 하면 시간초과..sort에서 시간 잡아먹나?
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    score = []
    anw = 1
    for j in range(N):
        score.append(list(map(int, input().split())))
    score.sort()
    win = score[0][1]
    for j in range(1, N):
        if score[j][1] < win:
            anw += 1
            win = score[j][1]
    print(anw)


# 정렬 안하고 서류 성적을 인덱스삼아 비교해도 시간초과..pypy는 통과 그냥 pypy로 풀래
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    score = [0,0] + [[0,0] for _ in range(N)]
    anw = 1
    for j in range(N):
        a, b = map(int, input().split())
        score[a] = b
    win = score[1]
    for j in range(2, N+1):
        if score[j] < win:
            anw += 1
            win = score[j]
    print(anw)