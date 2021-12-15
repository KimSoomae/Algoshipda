def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    matched = 0
    unknown = 0
    for idx in range(6):
        if lottos[idx] == 0:
            unknown += 1
        if lottos[idx] in win_nums:
            matched += 1
    answer.append(rank[matched + unknown])
    answer.append(rank[matched])
    return answer