import sys
sys.stdin = open('input.txt')
# [2, 7, 1, 2, 3] f(5) = f(4) + f(3) 
# [7, 1, 2, 3] = > f(4) = f(3)

# 1 ~ 34까지 적힌 숫자카드
# f(1) = 1
# f(2) = 1 or 2 합친게 34 이하라면 f(2) = 2, 34초과라면 f(2) = 1


# ni, nf = ni부터 nf까지 index를 가지는 리스트 집합? - nf = len(number)-1
# f(0, nf) = f(1, nf) + f(2, nf) if int(f(0, nf) + f(1, nf)) <= 34 else f(1, nf)

# f(nf, nf) = 1
# f(nf-1, nf) = f(nf, nf) + f(nf+1, nf) or f(nf, nf)
# f(nf-2, nf) = f(nf-1, nf) + 1 or f(nf-1, nf)

number = list(map(int, input()))

for i in range(len(number)): # 0카드가 없기 때문에 제거하는 과정
    if number[i] == 0:
        number[i-1] *= 10
while 0 in number:
    number.remove(0) #여기까지

n = len(number) # 리스트 길이
dp_memo = [1, 1] # 메모이제이션, dp(x-2)값을 계산해야 하기 떄문에 각 1, 1로 값을 설정

def dp(x):
    global dp_memo
    if x < 2:
        return dp_memo[x]
    else: # 초기 x = 5 ->  5 - x, 5 - (x-1) n = len(number)
        D = int(str(number[n-x]) + str(number[n-(x-1)]))
        if D > 34: #판별식 34초과라면 그 카드는 단일로 쓸수밖에 없음 : 35 ~ 4x
            if len(dp_memo) <= x:
                dp_memo.append(dp(x-1)) #메모에 추가
            return dp_memo[x]
        else:
            if len(dp_memo) <= x:
                dp_memo.append(dp(x-1) + dp(x-2))
            return dp_memo[x]

print(dp(n))

# YOSI!
