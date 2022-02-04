import datetime

today = datetime.date.today()
tdelta = datetime.timedelta(days=7)
one_week_ago = today - tdelta
next_week = today + tdelta

"""
How many days until my birthday
"""
birth_day = datetime.date(1990, 10, 18)

days_until_birthday = today - birth_day

print(days_until_birthday)

print(one_week_ago)
print(next_week)
