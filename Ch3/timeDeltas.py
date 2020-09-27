from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print("Today is: ", str(now))

# print today's date one year from now
print("One year from now it will be: ", str(now + timedelta(days=365)))

# create a time delta that uses more that one argument
print("In 2 days and 3 weeks, it will be " + str(now+timedelta(days=2, weeks=3)))

# calculate the date 1 week ago
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print ("One week ago it was: ", s)

# when is the next april fools day
today = date.today()
afd = date(today.year, 4, 1)
if afd < today:
	print("April fool's day already went by %d days ago" % ((today-afd).days))
	afd = afd.replace(year = today.year+1)

time_to_afd = afd-today
print("It's just ", time_to_afd.days, "days until April Fool's Day")