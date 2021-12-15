def solution(progresses, speeds):
    import math
    answer = []
    A = len(speeds)
    days = [0] * A
    for i in range(A):
        days[i] = math.ceil((100 - progresses[i]) / speeds[i])
    maxi = days[0]
    cnt = 1
    idx = 1
    while idx < A:
        if days[idx] > maxi:
            answer.append(cnt)
            maxi = days[idx]
            cnt = 1
        else:
            cnt += 1
        idx += 1
    answer.append(cnt)

    return answer