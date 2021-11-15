# 4195 친구 네트워크 - 유니온파인드 골드2 김수민
from collections import defaultdict
# 부모(친구관계) 찾기
def find_set(x):
    while x != friends[x]:
        x = friends[x]
    return x
# 친구 연결 + 친구관계 크기 리턴
def union(x, y):
    rootx = find_set(x)
    rooty = find_set(y)
    # 이미 친구면 바로 친구관계크기 리턴
    if rootx == rooty:
        return net[rootx]
    # 친구 아니면 유니온하고, 두 사람의 친구관계크기 합치기
    friends[max(rootx, rooty)] = min(rootx, rooty)
    net[rootx] = net[rootx] + net[rooty]
    net[rooty] = net[rootx]
    return net[rootx]
tc = int(input())
for _ in range(tc):
    # friends는 부모 담을 딕셔너리, net는 친구관계크기 담을 딕셔너리
    friends = defaultdict(str)
    net = defaultdict(int)
    N = int(input())
    for i in range(N):
        a, b = input().split()
        # 처음 등장한 친구면, 두 딕셔너리 초기화
        if len(friends[a]) == 0:
            net[a] = 1
            friends[a] = a
        if len(friends[b]) == 0:
            friends[b] = b
            net[b] = 1
        print(union(a, b))