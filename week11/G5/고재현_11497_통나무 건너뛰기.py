t = int(input())

for i in range(t):
    n = int(input())
    tree = list(map(int,input().split()))
    tree.sort()
    result = 0
    for j in range(0,n-2):
        m = tree[j+2] - tree[j]
        result = max(m, result)
    print(result)