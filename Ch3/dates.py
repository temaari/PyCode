from datetime import date
from datetime import time
from datetime import datetime

def main():
	## Date OBJECTS
	#Simple getting today's date
	# today = date.today()
	# print("Today's date is ", today)

	# # Print out indicidual components
	# print("Date components: ", today.day, today.month, today.year)

	# #
	# print("Today's weekday # is: ", today.weekday())
	# days = ["Mon","Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
	# print("Which is a: ", days[today.weekday()])

	# Time
	today = datetime.now()
	print("The current datetime is: ", today)

	t = datetime.time(datetime.now())
	print(t)


if __name__ == "__main__":
	main()