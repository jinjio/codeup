a, b = map(int, input().split())
boyRoom = [0,0,0]
girlRoom = [0,0,0]
RoomCount = 7
juniorGrade = 0


for i in range(a):
    gender, grade = map(int, input().split())
    if grade > 2:
        grade = int((grade-1)/2)

        if gender == 0:
            boyRoom[grade] += 1
            if boyRoom[grade] == b:
                boyRoom[grade] -= b
                RoomCount += 1
        else :
            girlRoom[grade] += 1
            if girlRoom[grade] == b:
                girlRoom[grade] -= b
                RoomCount += 1
    else:
        juniorGrade += 1
        if juniorGrade == b:
            juniorGrade -= b
            RoomCount += 1


for j in range(3):
    if boyRoom[j-1] == 0:
        RoomCount -= 1
for k in range(3):
    if girlRoom[k-1] == 0:
        RoomCount -= 1
if juniorGrade == 0:
    RoomCount -= 1

print(RoomCount)


