import sys
sys.stdin = open('input.txt')

sys.setrecursionlimit(10**6)
def binary(s, e, x):
    global res
    mid = (s+e) // 2
    if s > mid:
        res = 0
        return 
    if num_list[mid] < x:
        s = mid+1
        binary(s, e, x)
    elif num_list[mid] > x:
        e = mid-1
        binary(s, e, x)
    else:
        res = 1








n = int(input())
num_list = sorted(list(map(int, input().split())))

m = int(input())
search_list = list(map(int, input().split()))

for x in search_list:
    s = 0
    e = n-1
    res = 1
    binary(s, e, x)
    if res == 1:
        print(1)
    else:
        print(0)


