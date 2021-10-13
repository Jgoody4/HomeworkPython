# Import time
import time
# Create decorator
def calculate_time(func):
	"""
	This function will be used by the wrapper, hence it is the decorator.
	"""
	def wrapper():
		"""
		This function will save and print the time.
		-------------------------------------------
		Returns:
		--------
		wrapper = 
		"""
		start = time.time()
		func()
		finish = time.time()
		X = finish - start
		print(f'Total time {X}')
	return wrapper
