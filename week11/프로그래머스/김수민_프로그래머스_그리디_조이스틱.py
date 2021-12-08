def solution(name):
    answer = 0

    count = 0; i = 0
    while count < len(name):

        if i > 0 and name[i] == 'A':
            cnt = 1; cnt2 = 0
            for j in range(i+1, len(name)):
                if name[j] == 'A':
                    cnt += 1
                else:
                    break
            for j in range(len(name)-1, i, -1):
                if name[j] == 'A':
                    cnt2 += 1
                else:
                    break
            if cnt >= i + cnt2:
                answer += (i + cnt2) - 1
                count += cnt
                i += cnt
            else:
                answer += cnt
                i += cnt
                count+= cnt
        else:
            answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
            if i > 0: answer += 1
            i += 1
            count += 1


    print(answer)
    return answer

solution('JAZ')
solution('JEROEN')
solution('JAN')
solution('AABB')
solution('ABAAAAAAAAABB')