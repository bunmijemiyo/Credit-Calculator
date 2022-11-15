ref_day = "Tuesday"
time_zone = int(input())
if time_zone < -10:
    print("Monday")
elif time_zone > 13:
    print("Wednesday")
else:
    print(ref_day)
