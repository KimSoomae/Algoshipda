import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
arr = sorted([ int(input()) for _ in range(N)])

# 0(?) ~ 90
# mid = 45

#-----9----?
# 2*4 + 3*3 + 3*3 + 6*1 + 8*1 + 9*1 sum(i) = 13 not ok
# 9 % 2 + 9 % 3 + 9 % 3 + 9 % 6 + 9 % 9

#-----8----?
# 2*4 + 3*2 3*2 + 6*1 + 8*1 sum(i) = 10 ok


# ----7----?
# 2*3 + 3*2 + 3*2 + 6*1 sum(i) = 8 not ok

s = 0
e = max(arr) * M

while s <= e:
    mid = (s+e)//2

    value = 0
    for time in arr:
        if value > M:
            break
        if mid // time == 0:
            break
        
        value += mid // time
    
    if value >= M:
        e = mid -1
    else:
        s = mid + 1

print(s)
    


        

