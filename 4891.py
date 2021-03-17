n = int(input())
allScore = list(map(int, input().split()))

maxScore = 0
minScore = 100

for i in range(n):
    if allScore[i] > maxScore:
        maxScore = allScore[i]

for j in range(n):
    if allScore[j] < minScore:
        minScore = allScore[j]
    
print(maxScore-minScore)