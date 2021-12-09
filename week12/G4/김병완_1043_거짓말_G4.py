import sys; sys.stdin = open('1043_거짓말_G4.txt', 'r')
input = sys.stdin.readline

def find(x):
    if x != p[x]:
        p[x] = find(p[x])
    return p[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        x, y = y, x
    p[y] = x


N, M = map(int, input().split())
brighter = list(map(int, input().split()))[1:]
p = [i for i in range(N + 1)]
party = []
for _ in range(M):
    members = list(map(int, input().split()))[1:]
    party.append(members)

for i in range(M):
    for j in range(1, len(party[i])):
        a = party[i][j - 1]
        b = party[i][j]
        union(a, b)

for inParty in party:
    flag = False
    for mem in inParty:
        for k in range(len(brighter)):
            if find(brighter[k]) == find(mem):
                flag = True
                break
        if flag:
            M -= 1
            break

print(M)

