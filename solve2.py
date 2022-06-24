# # 완주하지 못한 선수
# def solution(participant, completion):
#     for i in range(len(completion)):
#         participant.remove(completion[i])        
#     answer = participant[0]
#     return answer
# def solution(participant, completion):
#     result = [n for n in participant if n not in completion]
#     answer = result[0]
# #     return answer
# def solution(participant, completion):
#     a = set(participant)
#     answer = 0
#     if len(participant) == len(a):
#         answer = list(set(participant)-set(completion))[0]
#         return answer
#     elif len(participant) > len(a):
#         for i in range(len(participant)):
#             numbers = participant.count(completion[i])
#             if numbers > 1:
#                 answer = completion[i]
#                 break
# #         return answer
def solution(participant, completion):
    a=len(set(participant)-set(completion))
    if a == 1 :
        answer = list(set(participant)-set(completion))[0]
    elif a != 1:
        for i in range(len(completion)):
            participant.remove(completion[i])
        answer = participant[0]
    return answer
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     a=set(participant)
#     b=set(completion)
#     c=len(a)-len(b)
#     d=list()
#     if c == 1:
#         answer = list(a-b)[0]
#     if c == 0:
#         a=list(a)
#         for i in range(len(a)):
#             d.append(participant.count(a[i]))
#         e=d.index(2)
#         answer=participant[e]
#     return answer
# print(solution(["leo","kiki","edan",],["edan","kiki",]))
# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))