import datetime

today = datetime.date.today()
tdelta = datetime.timedelta(days=7)
one_week_ago = today - tdelta
next_week = today + tdelta

print(one_week_ago)
print(next_week)
