def tripler(func):
	def wrapper(*args, **kwargs):
		func(*args, **kwargs)
		func(*args, **kwargs)
		func(*args, **kwargs)
	return wrapper()
@tripler
def say_whee():
	print("whee")

