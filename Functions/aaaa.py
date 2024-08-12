from datetime import date

today = date.today()

date_ = today.strftime("%d/%m/%Y")

a = date.weekday(today)

if a == 0:
    week_day = "Segunda"

print(a)