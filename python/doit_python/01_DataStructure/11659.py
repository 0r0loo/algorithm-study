import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

sumList = [0]
temp = 0

for i in arr:
    temp += i
    sumList.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    print(sumList[j] - sumList[i - 1])

