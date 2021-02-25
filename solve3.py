# 가운데 글자 가져오기
def solution(s):
    mid=0
    if len(s)%2==0:
        mid=int(len(s)/2)
        answer=s[mid-1:mid+1]
    else:
        mid=int(len(s)/2-0.5)
        answer=s[mid]
    return answer

print(solution('qwer'))