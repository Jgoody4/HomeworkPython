def tripler(func):
	"""
	This function is the decorator and will be used to call the function
	that this is used on three times. Here is a basic example below.
	"""
	def wrapper(*args, **kwargs):
		"""
		This is the wrapper function that the decorator decorates.
		"""
		func(*args, **kwargs)
		func(*args, **kwargs)
		func(*args, **kwargs)
	return wrapper
@tripler
def say_whee():
	"""
	Decorator operates on this function.
	"""
	print('Whee')

