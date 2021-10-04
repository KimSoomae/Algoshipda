N = int(input())
arr = list(map(int,input().split()))
anw = 0
while len(arr) > 1:
    maxv = max(arr)
    maxi = arr.index(maxv)
    if maxi > 0: a = arr[maxi-1]
    else: a = 0
    if maxi < len(arr)-1: b = arr[maxi+1]
    else: b = 0
    anw += min(maxv-a,maxv-b)
    del arr[maxi]
    # print(arr, anw)
print(anw)