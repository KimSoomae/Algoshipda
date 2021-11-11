import sys; sys.stdin = open('1107_리모컨_G5.txt', 'r')
input = sys.stdin.readline

def dfs(s, n):
    global result
    if s == n:
        num = int(''.join(map(str, nums)))
        result = min(abs(num - int(target)) + s, result)
        return
    else:
        for i in range(10):
            if not control[i]: continue
            nums.append(i)
            dfs(s + 1, n)
            nums.pop()

target = input().strip()
length = len(target)
M = int(input())
now = 100
result = abs(now - int(target))

brokens = []
if M > 0:
    brokens = map(int, input().split())
else:
    print(min(length, result))
    exit()

control = [True] * 10
for broken in brokens:
    control[broken] = False
nums = []

if M == 10:
    print(result)
    exit()

if result > length:
    for i in range(1, 8):
        dfs(0, i)
print(result)
