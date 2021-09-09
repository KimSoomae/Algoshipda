# import sys

# sys.stdin = open('영재의시험.txt', 'r')

def dfs(s):
    global cnt
    if s == 10:
        point = 0
        for j in range(10):
            if ans[j] == base[j]:
                point += 1
        if point >= 5:
            cnt += 1
        return
    for i in range(1, 6):
        if s > 1 and base[s - 2] == base[s - 1] == i:
            continue
        base.append(i)
        dfs(s + 1)
        base.pop()

ans = list(map(int, input().split()))
cnt = 0
base = []
dfs(0)
print(cnt)


