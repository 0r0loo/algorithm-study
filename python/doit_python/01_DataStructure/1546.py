n = int(input())
scoreList = list(map(int, input().split()))

maxScore = max(scoreList)

result = sum(scoreList) / maxScore * 100 / n

print(result)