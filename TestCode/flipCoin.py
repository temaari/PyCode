from random import randint

def main():
	while(True):
		print("HEADS!\n" if (randint(0,1) == 0) else "TAILS!\n")

		userInput = raw_input("Type \'EXIT\' or \'QUIT\' to leave or any other key to continue:\n")
		if (userInput.lower() == "exit" or userInput.lower() == "quit"):
			break

if __name__ == "__main__":
	main()