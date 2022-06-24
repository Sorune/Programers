# 더 맵게
scoville = [1, 2, 3, 9, 10, 12]
K=7
answer = 0
new_food=0
while True:
    scoville.sort()
    new_food=scoville[0]+scoville[1]*2
    scoville=scoville[2:]
    scoville.append(new_food)        
    answer +=1
    if min(scoville)>=K:
        break