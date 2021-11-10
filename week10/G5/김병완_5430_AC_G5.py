import sys; sys.stdin = open('5430_AC_G5.txt', 'r')
from collections import deque
input = sys.stdin.readline

def convert(arr):
    nums = deque()
    tmp = 0
    for string in arr:
        # 48 < ord <57
        if 48 <= ord(string) <= 57:
            tmp = tmp * 10 + int(string)
        elif ord(string) == 44:
            nums.append(tmp)
            tmp = 0
    if length != 0:
        nums.append(tmp)
    return nums

def rev(arr):
    tmp = deque()
    while arr:
        tmp.append(arr.pop())
    return tmp

def dele(arr, d):
    if len(arr) == 0:
        return -1
    if d == 1:
        arr.popleft()
    elif d == -1:
        arr.pop()
    return arr

# 규칙
# 1. R: 숫자 순서 뒤집기
# 2. D: 첫번째 숫자 버리기 > 비어있는데 쓰면 에러도출
# 함수 한번에 호출 가능 : RDD 뒤집고 첫번째 두번 버리기

for _ in range(int(input())):
    p = input()
    length = int(input())
    INPUT = input().strip()
    nums = convert(INPUT)
    d = 1

    for func in p:
        # 뒤집으라고 진짜 뒤집지 말자... 효율 좀 부탁이다
        if func == 'R':
            d *= -1
        elif func == 'D':
            nums = dele(nums, d)
        if nums == -1:
            break

# 출력은 띄어쓰기 없어야함..............(화가난다.)
    result = 'error'
    if nums != -1:
        if d == -1:
            nums = rev(nums)
        result = '[' + ','.join(map(str, nums)) + ']'

    print(result)




