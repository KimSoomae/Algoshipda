# 1107 리모컨 김수민
# 빡구현 실패..반례 다 못찾겠음 - 아마 자리수 넘어가서 누르는게 더 유리할때 이부부 고려해야될듯 ex 9999인데 9고장났으면 8888보다 10000이 유리
# 제욱님 설명 듣고 다시 풀어보기

def find(cnt, push):
    global anw  # +, - 버튼 눌러야되는 수 저장
    global flag # 앞 자리 잘 눌러졌는지 여부
    global bcnt # 숫자 버튼 누르는 수
    if cnt == n:
        if anw > abs(push - channel):
            anw = abs(push - channel)
        return

    if flag == False: # 앞에 재대로 눌렀으면
        if N[cnt] not in broken:
            find(cnt + 1, push + N[cnt] * pow(10, n-cnt-1))
        else:         # 고장났으면
            flag = True
            fflag = False
            tmp = 1        # +, - 1부터 해서 고장난거 없는 버튼으로 누른다
            while tmp <= 9:
                if N[cnt] + tmp not in broken and N[cnt] + tmp <= 9:       # 눌러야되는 수 + 1,2,3..
                    find(cnt + 1, push + (N[cnt] + tmp) * pow(10, n-cnt-1))
                    fflag = True
                if cnt == 0 and N[cnt] - tmp == 0 and n >= 2: # 11, 10과 같은 경우 자리수 줄여서 누르는게 더 유리할때
                    for k in range(9, 0, -1):
                        if k not in broken:
                            find(cnt + 2, push + k * pow(10, n - cnt - 2))
                            bcnt -= 1
                            break
                else:          # 눌러야되는 수  - 1,2,3..
                    if N[cnt] - tmp not in broken and N[cnt] - tmp >= 0:
                        find(cnt + 1, push + (N[cnt] - tmp) * pow(10, n - cnt - 1))
                        fflag = True
                if fflag == False:       # 둘다 고장났으면 +, - 할거를 늘린다
                    tmp += 1
                else:
                    break

    elif flag == True: # 앞에 제대로 안눌렀으면
        if (push // pow(10, n - cnt)) % 10 < N[cnt - 1]: # 앞에 5눌러야되는데 더 작은수면
            for i in range(9, -1, -1):
                if i not in broken:
                    find(cnt + 1, push + i*pow(10, n-cnt - 1))
                    break
        elif (push // pow(10, n - cnt)) % 10 > N[cnt - 1]: # 더 큰수면 최대한 작게 만들어야됨
            for i in range(10):
                if i not in broken:
                    find(cnt + 1, push + i*pow(10, n-cnt - 1))
                    break
        else:
            flag = False
            find(cnt + 1, push + (N[cnt] * pow(10, n - cnt - 1)))




channel =int(input())
N = list(map(int, str(channel)))
n = len(N) ; bcnt = n
m = int(input())
broken = list(map(int, input().split()))
anw = 10000000
flag = False
find(0, 0)
anw += bcnt # 버튼 누르는 수 더해준다
if anw > abs(100-channel):      # 100에서 +, - 버튼 누르는게 더 유리하면
    anw = abs(100-channel)

print(anw)

