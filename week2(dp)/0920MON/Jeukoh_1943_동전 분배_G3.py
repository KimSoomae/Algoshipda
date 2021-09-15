import sys; readline = sys.stdin.readline
def main():
    N = int(readline().strip())
    coin_list = [list(map(int, readline().split())) for _ in range(N)]
    tot = sum(map(lambda x: x[0] * x[1], coin_list))
    if tot%2:
        return 0
    needed = tot//2
    dp = [0]*(needed+1)
    dp[0] = 1
    coin_list.sort(reverse=True)
    maxm = 0
    for i in range(N):
        coin, num = coin_list[i]
        for now in range(min(needed,maxm),-1,-1):
            if dp[now]:
                # print(now,coin,num)
                if now + coin*num > needed:
                    dp[now+coin:now+coin*(num+1):coin] = [1]*(((needed-now-coin)//coin)+1)
                else:
                    dp[now + coin:now + coin * (num + 1):coin] = [1]*num
        if dp[needed]:
            return 1

        maxm += coin*num
    return 0


for _ in range(3):
    print(main())

#배열을 반으로 줄여도 if문 떄문에 시간은 더 오래걸린다. 메모리 차이는 얼마 안남;;
# 띠용
#---

''':var
import sys; readline = sys.stdin.readline
def main():
    N = int(readline().strip())
    coin_list = [list(map(int, readline().split())) for _ in range(N)]
    tot = sum(map(lambda x: x[0] * x[1], coin_list))
    if tot%2:
        return 0
    needed = tot//2
    dp = [0]*(tot+1)
    dp[0] = 1
    coin_list.sort(reverse=True)
    checked = 0
    for i in range(N):
        coin, num = coin_list[i]
        for now in range(min(needed,checked),-1,-1):
            if dp[now]:
                dp[now+coin:now+coin*(num+1):coin] = [1]*num
        if dp[needed]:
            return 1
        checked += coin*num
    return 0


for _ in range(3):
    print(main())

'''

#가장 잘나온 해.


#----

#시간 초과 pypy론 대긴함..
'''
import sys; readline = sys.stdin.readline
for _ in range(3):
    N = int(readline().strip())
    coin_list = [list(map(int,readline().split())) for _ in range(N)]
    needed = sum(map(lambda x: x[0]*x[1],coin_list))/2
    stack = [0]
    dp = {0:True}
    flag = True
    for i in range(N):
        coin, num = coin_list[i]
        tmp_stack = stack[:]
        while tmp_stack and flag:
            now = tmp_stack.pop()
            for n in range(num+1):
                if now+coin*n <= needed and not dp.get(now+coin*n):
                    dp[now+coin*n] = True
                    stack.append(now+coin*n)
                    if now+coin*n == needed:
                        flag = False
                        break
        if not flag:
            break

    if flag:
        print(0)
    else:
        print(1)
'''

