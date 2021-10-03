import sys
import math
sys.stdin = open('input.txt')

x, y, c = map(float, input().split())

s = 0; e = min(x, y)

while e - s > 0.0001 :
    mid = (s+e)/2

    hx = (x**2-mid**2)**0.5
    hy = (y**2-mid**2)**0.5

    c0 = (hx * hy) / ( hx + hy)

    if c0 >= c:
        s = mid+10**(-4)
    else:
        e = mid-10**(-4)

print("{:.3f}".format(mid))