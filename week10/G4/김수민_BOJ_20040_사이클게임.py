# 20040 사이클 게임 - 유니온파인드 G4 김수민

# 유니온 + 사이클 찾기
def union(x, y):
    rootx, rooty = find_set(x), find_set(y)
    # 부모가 같으면 사이클 형성
    if rootx == rooty:
        return True
    else:
        p[max(rootx, rooty)] = min(rootx, rooty)
        return False
# 부모 찾기
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

N, M = map(int, input().split())
p = [0] * N; anw = 0
for i in range(N):
    p[i] = i
for i in range(M):
    a, b = map(int, input().split())
    # 사이클 형성됐으면 몇번째인지 저장해서 break하고 아니면 간선 그어서 잇기
    if union(a, b):
        anw = i + 1
        break
print(anw)