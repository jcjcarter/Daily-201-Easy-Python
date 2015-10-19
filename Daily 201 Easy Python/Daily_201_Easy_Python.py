import datetime

d = [int(x) for x in input("Enter a date (yyyy-mm-dd): ").split('-')]

next_date = datetime.date(d[0], d[1], d[2])
today = datetime.date.today()
days_until = (next_date - today).days

print('{} days from {} to {}'.format(days_until, today, next_date))