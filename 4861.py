a, b = map(int, input().split())
boyRoom = [0,0,0,0,0,0]
girlRoom = [0,0,0,0,0,0]
RoomCount = 12

for i in range(a):
    gender, grade = map(int, input().split())
    if gender == 0:
        boyRoom[grade - 1] += 1
        if boyRoom[grade - 1] == b:
            RoomCount += 1
            boyRoom[grade - 1] -= b
    else :
        girlRoom[grade - 1] += 1
        if girlRoom[grade - 1] == b:
            RoomCount += 1
            girlRoom[grade - 1] -= b
for j in range(6):
    if boyRoom[j-1] == 0:
        RoomCount -= 1
for k in range(6):
    if girlRoom[k-1] == 0:
        RoomCount -= 1

print(RoomCount)

# 나머지로 푸는게 편할지도