import math

total = 0

n, m, p = map(int, input().split())

column = int((p-1)/m) 
row = (p-1) % m 

total += int(math.factorial(row + column) / (math.factorial(row) * math.factorial(column)))

column = n - column -1
row = m - row -1

total *= int(math.factorial(row + column) / (math.factorial(row) * math.factorial(column)))

print(total)
