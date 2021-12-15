from collections import defaultdict
def solution(clothes):
    answer = 1
    infos = defaultdict(list)
    for info in clothes:
        infos[info[1]].append(info[0])
    for key in infos:
        answer *= len(infos[key]) + 1
    answer -= 1
    return answer