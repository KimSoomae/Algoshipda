N,L = map(int, input().split())
street = [list(map(int, input().split())) for _ in range(N)]
result = 0
def check(street):
    road = [0] * N
    j = 0
    while j < N-1:
        if street[j] == street[j+1]:
            j += 1
            continue
        elif street[j] -1 == street[j+1]:
            target = street[j+1]
            count = 1
            for k in range(1, L):
                if road[j+k] == 1: break
                if j+1+k < N and target == street[j+1+k]:
                    count +=1
                else : break
            else:
                for x in range(1, L+1): road[j+x] = 1
                j += L
            if count < L : break
        elif street[j] +1 == street[j+1]:
            j -= L - 1
            if j < 0 : break
            target = street[j]
            count = 1
            if road[j] == 1 : break
            for k in range(1, L):
                if road[j+k] == 1: break
                if target == street[j + k]:
                    count += 1
                else:
                    break
            else:
                for x in range(0, L-1): road[j + x] = 1
                j += L
            if count < L: break
        else : break
    else :
        return True
#행
for i in range(N):
    if check(street[i]):
        result +=1
#열, transpose
street = list(zip(*street))
for i in range(N):
    if check(street[i]):
        result +=1
print(result)