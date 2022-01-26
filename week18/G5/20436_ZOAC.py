input = open('input.txt').readline

left, right = map(str, input().split())

left_keyboard = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v']
total_keyboard = {
    'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4), 'y': (0, 5), 'u': (0, 6), 'i': (0, 7), 'o': (0, 8), 'p': (0, 9),
    'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4), 'h': (1, 5), 'j': (1, 6), 'k': (1, 7), 'l': (1, 8),
    'z': (2, 0), 'x': (2, 1), 'c': (2, 2), 'v': (2, 3), 'b': (2, 4), 'n': (2, 5), 'm': (2, 6)
}

word = list(input())

result = 0
for ch in word:
    if ch in left_keyboard:
        if left == ch:
            result += 1
        else:
            x1, y1 = total_keyboard[left]
            x2, y2 = total_keyboard[ch]
            result += (abs(x1-x2) + abs(y1-y2)+1)
            left = ch
    else:
        if right == ch:
            result += 1

        else:
            x1, y1 = total_keyboard[right]
            x2, y2 = total_keyboard[ch]
            result += (abs(x1-x2) + abs(y1-y2)+1)
            right = ch          
print(result)