def swap_last_item(list):
	"""
	This program creates a function that takes in a list as input and then
	swaps the first and last elements of given elements in the list.
	----------------------------------------------------------------------
	Parameters
	----------
	list : List[]
		input of function is a list.
	Returns
	-------
	list : new List[]
		after swapping indexes the new List[] is returned.
	Examples
	--------
	list = [12, 35, 5, 9, 56, 24]
	after function call
	list = [24, 35, 5, 9, 56, 12]
	"""
	list[0], list[-1] = list[-1], list[0] # indexes of list getting swapped
	return list                           # returns the new list with indexes swapped
