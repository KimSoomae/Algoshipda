# BOJ 14888 연산자 끼워넣기(삼성SW역량테스트, 백트래킹) - 실버1 김수민
def dfs(i, tmp, pl, mi, mu, di):
    global maxanw, minanw
    if i == N:
        maxanw = max(maxanw, tmp)
        minanw = min(minanw, tmp)

    if pl > 0: # 쓸 수 있는 + 기호 남아있으면
        dfs(i + 1, tmp + arr[i], pl - 1, mi, mu, di)
    if mi > 0: # 쓸 수 있는 - 기호 남아있으면
        dfs(i + 1, tmp - arr[i], pl, mi - 1, mu, di)
    if mu > 0: # 쓸 수 있는 * 기호 남아있으면
        dfs(i+1, tmp * arr[i], pl, mi, mu -1, di)
    if di > 0: # 쓸 수 있는 // 기호 남아있으면
        if tmp < 0: # 음수일 경우 나눗셈 처리
            dfs(i + 1, -(abs(tmp) // arr[i]), pl, mi, mu, di-1)
        else:
            dfs(i + 1, tmp // arr[i], pl, mi, mu, di - 1)


N = int(input())
arr = list(map(int, input().split()))
pl, mi, mu, di = map(int, input().split())
maxanw = -100000000; minanw = 100000000
dfs(1, arr[0], pl, mi, mu, di)
print(maxanw)
print(minanw)