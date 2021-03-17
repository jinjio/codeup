n = int(input())

for i in range(n):
    scoreA = list(map(int, input().split()))
    scoreB = list(map(int, input().split()))

    scoreA[0] = 0
    scoreB[0] = 0

    totalA = list(map(lambda x: 101 ** x, scoreA))
    totalB = list(map(lambda x: 101 ** x, scoreB))

    SumA = sum(totalA)
    SumB = sum(totalB)

    if SumA < SumB:
        winner = 'B'
    elif SumA > SumB:
        winner = 'A'
    else:
        winner = 'D'


    print(winner)
    
# 