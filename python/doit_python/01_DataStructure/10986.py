n, m = map(int, input().split())
array = list(map(int, input().split()))

result = 0
sumList = [0] * n
count = [0] * m



for i in range(n):
    if i == 0:
        sumList[i] = array[i]
    else:
        sumList[i] = sumList[i - 1] + array[i]


for i in range(n):
    if sumList[i] % m == 0:
        result += 1
    count[sumList[i] % m] += 1

for i in range(m):
    result += count[i] * (count[i] - 1) // 2

print(result)



# 시간 초과
# n, m = map(int, input().split())
# array = list(map(int, input().split()))
#
# sumList = [0]
# temp = 0
#
# for num in array:
#     temp += num
#     sumList.append(temp)
#
# result = 0
#
# for i in range(n - 1):
#     for j in range(i + 1, n + 1):
#         if (sumList[j] - sumList[i]) % m == 0:
#             result += 1
#
# print(result)
