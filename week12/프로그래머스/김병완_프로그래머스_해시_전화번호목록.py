def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(1, len(phone_book)):
        length = len(phone_book[i - 1])
        if phone_book[i - 1] == phone_book[i][0:length]:
            return False
    return answer