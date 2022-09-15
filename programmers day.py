import datetime
today = datetime.datetime.now()
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
if day_of_year == 256:
    print("Happy Programmers Day!!!")
else:
    print("Today is -", day_of_year, "day of year.")