# import sys

# sys.stdin = open('김병완_16922_로마숫자만들기.txt', 'r')

def dfs(step, N, summation, n):
    global result
    if step == N:
        result[summation] = 1
        return
    else:
        for i in range(n, 4):
            dfs(step + 1, N, summation + rom_nums[i], i)


N = int(input())
rom_nums = [1, 5, 10, 50]
result = [0] * (50 * 20 + 1)
dfs(0, N, 0, 0)
ans = sum(result)
print(ans)