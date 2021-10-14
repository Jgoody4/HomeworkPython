def tripler(func):
	"""

	"""
	def wrapper():
		"""

		"""
		print("Inside wrapper function")
		func()
	print("Outside wrapper function")
	return wrapper

@tripler
def display():
	"""

	"""
	print("Inside display")
display()
display()
display()
