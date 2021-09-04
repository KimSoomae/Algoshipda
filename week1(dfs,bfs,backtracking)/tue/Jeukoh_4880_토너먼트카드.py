def divied(arr,N):
    def rcp(i, j):
        if arr[i] - arr[j] == 1 or arr[i] - arr[j] == -2:
            return i
        elif arr[i] == arr[j]:
            return i
        else:
            return j

    def partition(i,j):
        if i == j:
            return i
        left = partition(i,(i+j)//2)
        right = partition((i+j)//2+1,j)
        return rcp(left,right)
    return partition(1,N)
for tc in range(1,int(input())+1):
    N = int(input())
    arr = [0]+list(map(int,input().split()))
    print(f'#{tc} {divied(arr,N)}')