number_of_days = int(input())
temp_in_day = list(map(int, input().split()))

result = 0
if number_of_days == 1:
    print(1)
else:
    for day in range(len(temp_in_day)):
        if day != 0 and day != number_of_days - 1:
            if temp_in_day[day - 1] < temp_in_day[day] > temp_in_day[day + 1]:
                result += 1
        elif day == 0:
            if temp_in_day[day] > temp_in_day[day + 1]:
                result += 1
        elif day == number_of_days - 1:
            if temp_in_day[day] > temp_in_day[day - 1]:
                result += 1

    print(result)
