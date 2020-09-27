f = 0
# print(f)

# f = "abc"
# print(f)

# print("this is a string" + str(123))

def someFunction():
	global f
	f="def"
	print(f)

someFunction()
print(f)
del f
print(f) # Global name 'f' is not defined