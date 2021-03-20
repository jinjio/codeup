# import math
from math import gcd

n, m = map(int, input().split())

angle = []

for i in range(n, m+1):

    r = 360/i

    for j in range(i):
        if r * j in angle:
            # print('alredy has')
            a = 0
        else:
            angle.append(r * j)

print(len(angle))
