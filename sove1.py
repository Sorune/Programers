def solution(numbers):
    catalog=[]
    for i in range(len(numbers)):
        for l in range(len(numbers)):
            a=0
            a=numbers[i]+numbers[l]
            catalog.append(a)
        b=0
        b=numbers[i]*2
        catalog.remove(b)
    catalog=list(set(catalog))
    catalog.sort()
    answer = catalog
    return answer

print(solution([2,1,3,4,1]))