# 같은 숫자는 싫어 
def solution(arr):
    result=[]
    for i in range(len(arr)):
        if i < len(arr)-1:
            if arr[i]==arr[i+1]:
                pass            
            else:
                result.append(arr[i])
        else:
            result.append(arr[i])
    answer = result
    return answer

print(solution([1,1,3,3,0,1,1]))