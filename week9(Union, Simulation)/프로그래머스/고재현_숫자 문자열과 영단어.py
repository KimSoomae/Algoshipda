numbers_dict = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3',
    'four': '4', 'five': '5', 'six': '6', 'seven': '7',
    'eight': '8', 'nine': '9'
}
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def solution(s):
    answer = ''
    check = ''
    for i in range(len(s)):
        if s[i] in numbers:
            answer += s[i]
        else:
            check += s[i]
            if check in numbers_dict:
                answer += numbers_dict[check]
                check = ''


    return int(answer)

