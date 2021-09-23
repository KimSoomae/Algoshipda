X, Y, K = map(int,input().split())
def findcase(start,end):
    sx,sy = start
    ex,ey = end
    #print(start,end)
    dp = [[0]*(ey-sy+1) for _ in range(ex-sx+1)]
    for x in range(ex-sx+1):
        for y in range(ey-sy+1):
            if x == 0:
                dp[x][y] = 1
                continue
            if y == 0:
                dp[x][y] = 1
                continue
            dp[x][y] = dp[x-1][y] + dp[x][y-1]

    return dp[-1][-1]
if K:
    point = ((K-1)//Y,(K-1)%Y)
    anw = findcase((0,0),point)*findcase(point,(X-1,Y-1))
else:
    anw = findcase((0,0),(X-1,Y-1))

print(anw)