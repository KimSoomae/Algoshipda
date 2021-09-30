def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False


n = int(input())
card = list(map(int,input().split()))
m = int(input())
find = list(map(int,input().split()))
card.sort()
card_num = {}
for c in card:
    if c not in card_num:
        card_num[c] = 1
    else:
        card_num[c] += 1

for target in find:
    if binary_search(card,target,0,n-1):
        print(card_num[target], end=' ')
    else:
        print(0, end=' ')

