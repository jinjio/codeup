n = int(input())
arrMoney = []


for i in range(n):
    dices = list(map(int, input().split()))
    print(dices)
    diceSame = {}
    for n in dices:
        if n in diceSame:
            diceSame[n] += 1
        else:
            diceSame[n] = 1

    totalMoney = 0
    Max = 0
    two_count = 0
    two_count_val = 0

    for key in diceSame:
        count = diceSame[key]
        if count == 4:
            totalMoney = 50000 + key * 5000
        elif count == 3:
            totalMoney = 10000 + key * 1000
        elif count == 2:
            if two_count == 0:
                two_count += 1
                two_count_val = key
            else:        
                two_count += 1
                two_count_val += key
        else: 
            if key > Max:
                Max = key

    if two_count == 1:
        totalMoney = 1000 + 100 * two_count_val
    elif two_count == 2:
        totalMoney = 2000 + 500 * two_count_val
    elif totalMoney == 0:
        totalMoney = Max * 100

    arrMoney.append(totalMoney)

print(max(arrMoney))        