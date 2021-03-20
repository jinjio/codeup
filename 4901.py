import math

n = int(input())
pList = []

total = 0

for i in range(n):
    pList += list(map(int, input().split()))

# print(pList)

for j in range(n):
    # k = 0
    s = 0
    for k in range(n):
        dscTotal = 1000000001
        ascTotal = 1000000001
        if ((j + 2 + k + s) * 2 - 1) <= len(pList):
            if pList[(j+1)*2-1] == pList[(j+2+k)*2-1]:
                # print(pList[(j+2+k) * 2 - 2])
                ascTotal = abs(pList[(j+1) * 2 - 2] - pList[(j+2+k) * 2 - 2])
                print(abs(pList[(j+1) * 2 - 2] - pList[(j+2+k) * 2 - 2]))

        if (j - k) <= 0:
            if pList[(j+1)*2-1] == pList[(j-k)*2-1]:
                # print(pList[(j-k) * 2 - 2])
                dscTotal = abs(pList[(j+1) * 2 - 2] - pList[(j-k) * 2 - 2])

        if dscTotal != 1000000001 or ascTotal != 1000000001:
            if ascTotal > dscTotal:
                total = dscTotal
                print(dscTotal)
                s = n
                continue
            else:
                total = ascTotal
                s = n
                continue

print(total)
