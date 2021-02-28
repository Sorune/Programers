def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        list_1=commands[i]
        list_2=[]
        list_2 = array[list_1[0]-1:list_1[1]]
        list_2.sort()
        answer.append(list_2[list_1[2]-1])
    
    return answer

print(solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]]))