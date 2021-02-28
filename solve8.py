# 문자열을 정수로 바꾸기
def solution(s):
    answer =0
    if ord(s[0])==43:
        answer += int(s[1:])
    elif ord(s[0])==45:
        answer-= int(s[1:])
    else:
        answer+=int(s)
    return answer

print(solution('-1234'))