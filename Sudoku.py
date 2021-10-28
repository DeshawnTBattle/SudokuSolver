def load_puzzle(path):
	with open (path, 'r') as fh:
		contents = fh.read()
		lines = contents.split('\n')
		puzzle = []
		for line in lines:
			token_strings = line.split(' ')
			token_ints = [int(i) for i in token_strings]
			puzzle.append(token_ints)
		return puzzle

def display_puzzle(puzzle):
	for line_index,line in enumerate(puzzle):
		if line_index in [0, 3, 6]:
			print("+------+------+------+")
		row = "|"
		for item_index, item in enumerate(line):
			if item == 0:
				row += ". "
			else:
				row += str(item) + " "
			if item_index in [2, 5, 8]:
				row += "|"
		print(row)
	print("+------+------+------+")



def get_next(row,col):
	if col < 8:
		return row, col+1
	if col == 8 and row < 8:
		return row+1, 0
	if col == 8 and row == 8:
		return None, None


def copy_puzzle(puzzle):
	new_puzzle = []
	for items in puzzle:
		new_puzzle.append(items.copy())
	return new_puzzle


def get_options(puzzle, row, col):
	
	if puzzle[row][col] > 0:
		return None

	used = []

	#scanning row
	for element in puzzle[row]:
		if element > 0:
			used.append(element)

	#Scanning cols
	for lines in puzzle:
		if lines[col] > 0:
			used.append(lines[col])

	#Scanning 3*3
	start_row = 3*int(row/3)
	start_col = 3*int(col/3)
	for i in range(start_row, start_row + 3):
		for j in range(start_col, start_col + 3):
			if puzzle[i][j] > 0:
				used.append(puzzle[i][j])

	options = []
	for i in range(1,10):
		if i not in used:
			options.append(i)
	return options


def solve(puzzle, row, col):
	if puzzle[row][col] > 0:
		next_row, next_col = get_next(row, col)
		if next_row is None:
			return puzzle
		else:
			result = solve(puzzle, next_row, next_col)
			if result is not None:
				return result
	else:
		options = get_options(puzzle, row, col)
		if options is None or len(options) == 0:
			return None
		for element in options:
			new_puzzle = copy_puzzle(puzzle)
			new_puzzle[row][col] = element
			result = solve(new_puzzle, row, col)
			if result is not None:
				return result