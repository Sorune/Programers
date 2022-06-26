# 수박수박수박수박수박수?
def solution(n):
    answer="수박"*(int(n/2))
    if n % 2 == 1:
        answer +='수'
    else:
        pass
    return answer

print(solution(9))