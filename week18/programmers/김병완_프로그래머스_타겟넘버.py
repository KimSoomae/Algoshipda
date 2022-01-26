def dfs(n, s, cur_sum, goal, lis):
    global answer
    if s == n:
        if cur_sum == goal:
            answer += 1
    else:
        for i in [-1, 1]:
            tmp = cur_sum + lis[n] * i
            dfs(n + 1, s, tmp, goal, lis)

def solution(numbers, target):
    global answer
    answer = 0
    N = len(numbers)
    dfs(0, N, 0, target, numbers)
    return answer

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    goal = int(input())
    print(solution(nums, goal))