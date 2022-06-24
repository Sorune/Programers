# 가장 큰 수
numbers = [ 6, 10, 2]
sum_results = []
numbers_rematch = numbers
for i in range(len(numbers)*len(numbers)):
    number = ''
    for l in range(len(numbers)):
        number += str(numbers_rematch[l])
        if l == len(numbers)-1:
            sum_results.append(int(number))
    number = ''
    for j in range(len(numbers)-1,-1,-1):
        number += str(numbers_rematch[j])
        if j == 0:
            sum_results.append(int(number))
    extention = numbers_rematch[0]
    numbers_rematch.pop(0)
    numbers_rematch.append(extention)
answer = str(max(sum_results))
print(answer)