def quadratic_solutions(a, b, c):
	disc = b**2 - 4 * a * c
	if(disc > 0):
		return 2
	else if(disc == 0):
		return 1
	else:
		return 0