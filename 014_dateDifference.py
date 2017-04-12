from datetime import date

date1 = date.today()
date2 = date(2015, 12, 22)
difference = date1 - date2
print(difference.days)