# 문자열 다루기 기본
def solution(s):
    text=list(s)
    num=[x for x in range(48,58)]
    if len(text)==4 or len(text)==6:
        result = list(filter(lambda n : ord(n) in num, text))
        if len(result)==len(text):
            answer=True
        else :
            answer=False
    else :
        answer=False
    return answer
print(solution("a234"))
    