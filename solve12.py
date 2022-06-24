# 숫자의 표현
number = 15
result = []
numbers = range(1,number+1)
instant_num=0
for i in range(number):
    instant_num += numbers[i]
    if instant_num == number:
        result.append(instant_num)
        instant_num = 0
    elif instant_num > number:
        instant_num = 0
for l in range(number,-1,-1):
    instant_num += numbers[i]
    if instant_num == number:
        result.append(instant_num)
        instant_num = 0
    elif instant_num > number:
        instant_num = 0
print(result)