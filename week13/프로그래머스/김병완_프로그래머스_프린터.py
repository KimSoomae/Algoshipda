def solution(priorities, location):
    from collections import deque
    answer = 0
    tmp = deque()
    for idx in range(len(priorities)):
        tmp.append((priorities[idx], idx))
    while tmp:
        pr, i = tmp.popleft()
        for t in tmp:
            if t[0] > pr:
                tmp.append((pr, i))
                break
        else:
            answer += 1
            if i == location:
                break
    return answer