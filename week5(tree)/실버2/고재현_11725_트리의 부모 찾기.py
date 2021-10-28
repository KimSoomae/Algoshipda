n = int(input())
lst = [0] * (n+1)
lst[0], lst[1] = -1, -1
for i in range(n-1):
    a,b = map(int,input().split())
    if lst[a] == 0:
        lst[a] = b
    else:
        lst[b] = a
for i in range(2,n):
    print(lst[i])