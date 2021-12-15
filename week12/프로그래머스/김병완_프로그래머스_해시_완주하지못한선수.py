def solution(participant, completion):
    answer = ''
    tmp = {}
    for part in participant:
        if not part in tmp:
            tmp[part] = 1
        else:
            tmp[part] += 1
    for comp in completion:
        tmp[comp] -= 1
    for temp in tmp:
        if tmp[temp]:
            answer = temp
            break
    return answer
