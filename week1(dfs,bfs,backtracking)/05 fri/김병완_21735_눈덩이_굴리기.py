# import sys
#
# sys.stdin = open('눈덩이_굴리기.txt', 'r')

N, M = map(int, input().split())
rail = list(map(int, input().split()))

def dfs(step, idx):
    global maxi
    if step == M:
        if S[-1] >= maxi:
            maxi = S[-1]
            return
    else:
        for i in range(2):
            if i == 0:
                idx += 1
                if idx >= N:
                    if maxi <= S[-1]:
                        maxi = S[-1]
                    idx -= 1
                    return
                S.append(S[-1] + rail[idx])
                dfs(step + 1, idx)
                S.pop()
                idx -= 1

            else:
                idx += 2
                if idx >= N:
                    if maxi <= S[-1]:
                        maxi = S[-1]
                    idx -= 2
                    return
                tmp = S[-1] >> 1
                tmp += rail[idx]
                S.append(tmp)
                dfs(step + 1, idx)
                S.pop()
                idx -= 2

S = [1]
maxi = -1
dfs(0, -1)
print(maxi)
