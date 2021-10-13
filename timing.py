# Import time
import time
# Create decorator
def calculate_time(func):
	def wrapper():
		start = time.time()
		func()
		finish = time.time()
		print("Total time ", finish - start)
	return wrapper
calculate_time()

