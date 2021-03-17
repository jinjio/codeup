n = int(input())
sumApple = 0
restApple = 0

for i in range(n):
    num1, num2 = map(int, input().split())
    while (sumApple + 1) * num1 <= num2 :
        sumApple += 1
    restApple += num2 - sumApple * num1
    sumApple = 0

print(restApple)