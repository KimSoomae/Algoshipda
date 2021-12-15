def solution(genres, plays):
    from collections import defaultdict
    answer = []
    info = defaultdict(list)
    gen_rank = defaultdict(int)
    A = len(genres)
    for i in range(A):
        info[genres[i]].append((plays[i], i))
        gen_rank[genres[i]] += plays[i]
    gen_rank = dict(sorted(gen_rank.items(), key=lambda x: -x[1]))

    for key in gen_rank:
        if gen_rank[key] > 0:
            info[key].sort(key=lambda x: x[0], reverse=True)
            if len(info[key]) == 1:
                answer.append(info[key][0][1])
            else:
                for i in range(2):
                    answer.append(info[key][i][1])
    return answer