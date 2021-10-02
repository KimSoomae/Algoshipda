# 1300 k번째수 - 시간초과 노답 코드^^

# N보다 작은 약수의 개수 구하기
def getMyDivisor(n):
    tmp = 0
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            if ((i ** 2) == n) and (i <= N):
                tmp += 1
            elif i <= N and n // i <= N:
                tmp += 2
    return tmp

def find(m, bm, bn):
    # 구해야되는 인덱스가 전에 구한거보다 크면
    if bm < m:
        for i in range(bn + 1, N * N + 1):
            # 약수의 개수 더해주면서 순서 더해준다
            bm += divide[i]
            if bm >= m:
                # 이때 i는 m번째에 저장된 수
                return [bm, i]
    # 구해야되는 인덱스가 전에 구한거보다 작으면
    elif bm > m:
        for i in range(bn, 0, -1):
            bm -= divide[i]
            if bm == m:
                continue
            elif bm < m:
                return [bm + divide[i], i]
    else:
        return [bm, bn]

N = int(input())
K = int(input()) - 1
L = 0; R = N * N - 1
anw = 0
before_mid = 0
before_n = 1
divide = [0]
# N을 넘어가지 않는 약수의 개수 저장
for i in range(1, N * N + 1):
    divide.append(getMyDivisor(i))
while L <= R:
    # mid는 탐색중인 인덱스
    mid = (L + R) // 2
    # mid번째에 저장된 값을 약수 개수의 합을 통해 구한다
    n = find(mid, before_mid, before_n)
    before_mid = n[0] # 다음 이분탐색 때 첨부터 안세고 탐색마친데 부터 세려고 저장하는 인덱스
    before_n = n[1] # 얘도 저장하는 수
    if mid == K or before_mid == K:
        anw = before_n
        break
    elif mid < K:
        L = mid + 1
    else:
        R = mid - 1
print(anw)