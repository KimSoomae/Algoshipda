def binary_search(arr, find, start, end):
    while start <= end:
        mid_idx = (start + end) // 2
        if arr[mid_idx] == find:
            return 1
        elif arr[mid_idx] < find:
            start = mid_idx + 1
        else:
            end = mid_idx -1
    return 0

n = int(input())
A = list(map(int,input().split()))
m = int(input())
find_list = list(map(int,input().split()))
A.sort()
for find in find_list:
    print(binary_search(A,find,0,n-1))