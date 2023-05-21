n = int(input())

result = 1
start = 1
end = 1
sum = 1

while end != n:
    if sum == n:
        print(sum , start, end)
        result += 1
        sum -= start
        start += 1
    elif sum < n:
        end += 1
        sum += end
    else:
        sum -= start
        start += 1

print(result)