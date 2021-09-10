# import sys
#
# sys.stdin = open('태권왕.txt', 'r')

def dfs(step, S, T):
    global mini
    if S == T:
        if step <= mini:
            mini = step
            return
    elif S > T:
        return
    else:
        for i in range(2):
            if i == 0:
                S += S
                T += 3
                dfs(step + 1, S, T)
                S -= S >> 1
                T -= 3
            else:
                S += 1
                dfs(step + 1, S, T)
                S -= 1


for tc in range(int(input())):
    S, T = map(int, input().split())

    mini = 1000
    dfs(0, S, T)
    print(mini)

