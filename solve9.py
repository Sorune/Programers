# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
# 입출력 예
# arr1	arr2	return
# [[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
# [[1],[2]]	[[3],[4]]	[[4],[6]]
arr1=[[1,2],[3,4]]
arr2=[[3,4],[5,6]]
answer = [[]]
print(arr1[1][1])
print(arr2[1][1])
print(arr1[1][1]+arr2[1][1])
sub=[]
for i in range(len(arr1)):
    answer.insert(i,arr1[i][i]+arr2[i][i])
answer.pop()
print(answer)