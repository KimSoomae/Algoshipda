import sys; sys.stdin = open('9935_문자열폭발_G4.txt', 'r')
from collections import deque
input = sys.stdin.readline

string = input().strip()
bomb = input().strip()
bomb_len = len(bomb)
stack = []
# stack.append(string[0])

for idx in range(len(string)):
    stack.append(string[idx])
    if stack[-1] == bomb[-1]:
        start = len(stack) - bomb_len
        if start < 0: continue
        end = len(stack)
        cnt = 0
        for i in range(start, end):
            if stack[i] == bomb[i - start]:
                cnt += 1
        if cnt == bomb_len:
            for k in range(bomb_len):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')
