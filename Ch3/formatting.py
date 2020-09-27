from datetime import datetime

def main():
	#Times and dates can be formated

	now = datetime.now()

	### some date formatting
	# print(now.strftime("The current year is: %Y"))
	# print(now.strftime("%a, %d, %B, %y"))

	### locale
	# print(now.strftime("Local date and time: %c"))
	# print(now.strftime("Local date: %x"))
	# print(now.strftime("Local time: %X"))

	#Tine formatting
	print(now.strftime("Current time: %I:%M:%S %p"))
	print(now.strftime("24-Hour time: %H:%M"))

if __name__ == "__main__":
	main()