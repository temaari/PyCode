# import the calender module
import calendar

# create plain text calender
c = calendar.TextCalendar(calendar.SUNDAY)
# st = c.formatmonth(2017, 1, 0, 0)
# print(st)

# create a html formatted calender
# hc = calendar.HTMLCalendar(calendar.MONDAY)
# st = hc.formatmonth(2017, 1)
# print(st)

# loop over days of a month
# for i in c.itermonthdays(2017, 8):
# 	print(i)

# current local
# for name in calendar.month_name:
# 	print(name)

# for day in calendar.day_name:
# 	print(day)

# Calculate days based on a rule
print("Team meetings will be on: ")
for m in range(1,13):
	cal = calendar.monthcalendar(2018, m)
	weekone = cal[0]
	weektwo = cal[1]

	if weekone[calendar.FRIDAY] != 0:
		meetday = weekone[calendar.FRIDAY]
	else:
		meetday = weektwo[calendar.FRIDAY]
	
	print("%10s %2d" % (calendar.month_name[m], meetday))