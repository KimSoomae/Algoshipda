import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
# sys.stdin = open('김병완_1520_내리막길_G4.txt', 'r')
# 시간 초과....
def dfs(r, c, arr, M, N):
    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    if r == M - 1 and c == N - 1:
        return 1
    elif arr2[r][c]:
        return arr2[r][c]
    else:
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr < 0 or nr >= M or nc < 0 or nc >= N: continue
            if arr[r][c] <= arr[nr][nc]: continue
            arr2[r][c] += dfs(nr, nc, arr, M, N)
        return arr2[r][c]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
# dp용 리스트
arr2 = [[0] * N for _ in range(M)]
dfs(0, 0, arr, M, N)

# print(arr2, cnt)
print(arr2[0][0])