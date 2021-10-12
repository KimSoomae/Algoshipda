input = open('input.txt').readline
N = int(input())
choo_weight = list(map(int, input().split()))
max_weight = sum(choo_weight)
dp_memo = [False] * (max_weight + 1)
dp_memo[0] = True

for choo in choo_weight: #넣고싶은 추의 각 원소
    arr = dp_memo.copy()
    for index, chk in enumerate(arr):
        if chk and not dp_memo[index + choo]:
            dp_memo[index + choo] = True

for choo in (choo_weight): #빼고싶은 추의 각 원소
    arr = dp_memo.copy()
    for index, chk in enumerate(arr):
        if (index - choo) >= 0:
            if chk and not dp_memo[index - choo]:
                dp_memo[index - choo] = True

M = int(input())
Q_list = list(map(int, input().split()))

for Q in Q_list:
    if Q > max_weight:
        print('N', end= ' ')
    elif dp_memo[Q]:
        print('Y', end= ' ')
    else:
        print('N', end= ' ')
