n = int(input())
A = 300
B = 60
C = 10

countA = int(n/A) 
countB = int((n%A)/B)
countC = int(((n%A)%B)/C)
if int(((n%A)%B)%C) != 0:
    print(-1)
else:
    print(countA, countB, countC)


