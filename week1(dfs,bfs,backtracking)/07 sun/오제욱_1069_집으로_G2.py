import sys; readline = sys.stdin.readline
X,Y,D,T = map(int,readline().split())
dist = (X**2+Y**2)**(1/2)
eff = D/T
anw = 0
if eff < 1:
    anw = dist
else:
    if dist == D:
        anw = min(T,dist)
    else:
        while dist > 2*D:
            anw += T
            dist -= D
        tmp = min(2*T,dist,T+abs(D-dist))
        anw += tmp
print(f'{anw:.10f}')