# 완주하지 못한 선수
# def solution(participant, completion):
#     for i in range(len(completion)):
#         participant.remove(completion[i])        
#     answer = participant[0]
# #     return answer
# def solution(participant, completion):
#     result = [n for n in participant if n not in completion]
#     answer = result[0]
#     return answer
def solution(participant, completion):
    result = list(set(participant)-set(completion))
    answer = result[0]
    return answer
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))
