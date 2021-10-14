def tripler(func):
	def wrapper():
		func()
		func()
		func()
	return wrapper()
@tripler
def say_whee():
	print("whee")

