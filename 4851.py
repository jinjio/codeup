n = int(input()) 
m = int(input())

for i in range(m): 
    a, b = map(int, input().split())

    if a > b :
        if a * 2 - 2 > n + b:
            print(0)
        else:
            print(1)
    elif a < b:
        if b * 2 - 2 >= n + a:
            print(0)
        else:
            print(1)
    else :
        print(1)

    # if max(players) * 2 - 2 >= n + min(players):
    #     print(0)
    # else: 
    #     print(1)    
