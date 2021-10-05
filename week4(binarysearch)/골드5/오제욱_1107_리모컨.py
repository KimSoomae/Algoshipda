# end = int(input().strip())
# N = int(input())
# if N:
#     cease = input().split()
# else:
#     cease = []
#
# start = 100
#
# # 1 올 버튼 +,-
# anw1 = abs(end-start)
#
# # 2 키패로 눌러서 갈 수 있는 가장 가까운 낮은 수 +버튼
#
# cnt1 = 0
# s = end
# while cnt1 < anw1:
#     for x in list(str(s)):
#         if x in cease:
#             s -= 1
#             cnt1 += 1
#             break
#     else:
#         break
#
# anw2 = len(str(s)) + cnt1
# anw = min(anw1,anw2)
#
# # 3 가장 가까운 높은 수 + 버튼
# cnt1 = 0
# s = end
# while cnt1 < anw:
#     for x in list(str(s)):
#         if x in cease:
#             s += 1
#             cnt1 += 1
#             break
#     else:
#         break
#
# anw2 = len(str(s)) + cnt1
# anw = min(anw,anw2)
# print(anw)
#
#
#
# # 이분 탐색 좋은 문제
#
# class Remocon:
#     def __init__(self):
#         self.buttons = list(range(10))
#
#     def distroy(self, b):
#         self.buttons.remove(b)
#
#
#
#     def __getitem__(self, n):
#         l = len(self.buttons)
#         result, digit = 0, 1
#         while n >= l:
#             result += self.buttons[n % l] * digit
#             n //= l
#             if self.buttons[0]:
#                 n -= 1
#             digit *= 10
#         result += self.buttons[n % l] * digit
#         return result
#
#     def least_button_push(self, target):
#         if not self.buttons:
#             result = float('inf')
#         elif self.buttons == [0, ]:
#             result = target + 1
#         elif self[0] > target:
#             result = self[0] - target + 1
#         else:
#             lo, hi = 0, 10
#             while self[hi] <= target:
#                 hi *= 10
#             while hi - lo > 1:
#                 m = (lo + hi) // 2
#                 if self[m] < target:
#                     lo = m
#                 else:
#                     hi = m
#             lower, higher = self[lo], self[hi]
#             result = min(len(str(lower)) + abs(lower - target),
#                          len(str(higher)) + abs(higher - target))
#
#         return min(result, abs(target - 100))
#
#
# remocon = Remocon()
# target = int(input())
# if int(input()):
#     for button in map(int, input().split()):
#         remocon.distroy(button)
# print(remocon.least_button_push(target))