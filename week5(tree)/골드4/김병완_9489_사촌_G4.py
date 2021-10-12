import sys; sys.stdin = open('김병완_9489_사촌_G4.txt', 'r')
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

# def dfs(n, lev):
#     if tree[n] == False:
#         if lev in level:
#             level[lev] += [n]
#         else:
#             level[lev] = [n]
#     else:
#         if lev in level:
#             level[lev] += [n]
#         else:
#             level[lev] = [n]
#         for key in tree[n]:
#             dfs(key, lev + 1)

while 1:
    N, K = map(int, input().split())
    if N == 0 and K == 0: break
    nums = list(map(int, input().split()))
    tree = {num: [] for num in nums}
    key_idx = 0
    for idx in range(1, N):
        if nums[idx - 1] != nums[idx] - 1:
            key = nums[key_idx]
            key_idx += 1
            tree[key].append(nums[idx])
        else:
            tree[key].append(nums[idx])

    # level = {1: [], 2: []}
    # dfs(nums[0], 1)
    sibling_key = 0
    cousin = 0
    for key, value in tree.items():
        if K in value:
            sibling_key = key
    for key1, value in tree.items():
        if sibling_key in value:
            for key2 in tree[key1]:
                if key2 == sibling_key: continue
                cousin += len(tree[key2])
    print(cousin)
