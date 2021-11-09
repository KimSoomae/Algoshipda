def find_rank(num):
    if num == 0:
        return 6
    else:
        return 7 - num


def solution(lottos, win_nums):
    cnt0 = 0
    ans = 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            cnt0 += 1
        else:
            for j in range(len(win_nums)):
                if lottos[i] == win_nums[j]:
                    ans += 1

    max_num = ans + cnt0
    min_num = ans
    answer = [find_rank(max_num), find_rank(min_num)]
    return answer

