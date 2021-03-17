A, B, C, Total = map(int, input().split())
i = 0

while (C * i) <= Total:
    j=0
    while (B * j) <= Total:
        k = 0
        while (A * k) <= Total:
            if (C * i) + (B * j) + (A * k) == Total:
                print(1)
                quit()
            k += 1
        j += 1
    i += 1

print(0)
# if int(((Total%C)%B)%A) == 0:
#     print(1)
# else:
#     print(0)
