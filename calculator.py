def calculator(number1, number2, operator):
	"""
	This function performs as a calculator that takes user input and
	performs mathematical operations, ie. add, sub, mult, div, floor div, and power.
	--------------------------------------------------------------------------------
	Parameters
	----------
	number1 = List[]
	operator = List[]
	number2 = List[]
		all assigned from user input using split().
	Returns
	-------
	operator = List[]
		calculator returns a result using an if else.
	"""
	if operator == "+":
		print(number1 + number2)
	elif operator == "-":
		print(number1 - number2)
	elif operator == "*":
		print(number1 * number2)
	elif operator == "/":
		return 0 if number2 == 0 else print(number1 / number2)
	elif operator == "//":
		print(number1 // number2)
	elif operator == "**":
		print(number1 ** number2)
	else:
		return False
def parse_input():
	"""
	This function parses users input from the split() function. It then
	assigns the values in a List[] and calls the calculator() function.
	-------------------------------------------------------------------
	"""
	# While user enters a valid equation
	while True:
		# User input is parsed using the split() function
		# Variables being set to be used in the calculator call
		equation = input("Enter equation: ").split()
		op = equation[1]
		num1 = float(equation[0])
		num2 = float(equation[2])
		# Checking if the operator is valid input else break
		if not (op=="+" or op=="-" or op=="*" or op=="/" or op=="//" or op=="**"):
			break
		# Function call to calculator() with parameters
		calculator(num1, num2, op)
		break
parse_input()
