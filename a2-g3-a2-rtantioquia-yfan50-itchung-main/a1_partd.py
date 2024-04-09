#    Main Author(s): In Tae Chung
#    Main Reviewer(s):

import copy

from a1_partc import Queue

"""
get_overflow_list(grid)

argument: 
grid - 2D array (python lists) of numbers 

functionality:
for each "cell" in the 2D array, the cells directly above, below, right, and left 
of the cell is checked to see if it contains a non-zero value.
If the value in the cell being checked is greater or equal 
to the number of adjacent cells with values,
those coordinates are appended to a list.

If cells will overflow, those cell coordinates are returned as a list.
Else, function returns None
"""
def get_overflow_list(grid):
	if grid:
		# gets the number of rows
		rows = len(grid)
		# gets the number of columns
		cols = len(grid[0])

		# create an empty list to store values that are in overflow
		overflow_list = []

		# iterating over each "cell" in grid by going over each row x col
		for i in range(rows):
			for j in range(cols):
				# counter to see if cell is in overflow
				count = 0

				# increase counter if not the top row
				if i > 0:
					count += 1

				# increase counter if not the bottom row
				if i < rows - 1:
					count += 1

				# increase counter if not the first column
				if j > 0:
					count += 1
				
				# increase counter if not the last column
				if j < cols - 1:
					count += 1

				# if the absolute value of the cell is greater or equal to the counter, 
				# append the cell coordinates to the overflow list
				if abs(grid[i][j]) >= count:
					overflow_list.append((i,j))
				
		# return overflow_list if not empty
		if overflow_list:
			return overflow_list
		else:
			return None


"""
arguments:
grid - 2D array (python lists) of numbers 
a_queue - instance of Queue data structure partc)

This function call get_overflow_list to see if there are any cells overflowing
If overflow is not occuring or all the cells are of the same pos/neg sign,
nothing happens and zero is returned

If there are cells in overflow, that cell is reset to zero,
and all adjacent cells are increased in value by 1 or -1.
If the overflowing cell's value was negative, the adjacent cell also becomes negative

This new grid is enqueued to the a_queue

The function returns how many grids were added to the a_queue 
before the base condition was reached.

"""
def overflow(grid, a_queue):
# base case: overflow is not happening or all cells are same sign
	
	# get list of cells in overflow
	overflow_nums = get_overflow_list(grid)

	# check if all elements in the grid have the same sign
	all_pos = True
	all_neg = True
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] < 0:
				all_pos = False
			if grid[i][j] > 0:
				all_neg = False

	# if there are no cells overflowing
	# or all numbers are positive or negative, do nothing
	if overflow_nums is None or all_pos or all_neg:
		return 0

# general case:

	# #create copy to grid to manipulate
	new_grid = copy.deepcopy(grid)

	# for the coordinates of cells in overflow
	for i, j in overflow_nums:
		grid[i][j] = 0

	for i, j in overflow_nums:
		# cells adjacent to overflow will increase their value by 1
		# ensuring signs are changed based on sign of overflowing cell
		for x, y in [(i - 1, j), (i + 1, j), (i,j - 1), (i, j + 1)]:
			# increase adjacent cell's absolute values by 1
			if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
				abs_value = abs(grid[x][y]) + 1

				# change the adjacent cell's sign to sign of overflow
				if new_grid[i][j] < 0:
					grid[x][y] = -abs_value
				else:
					grid[x][y] = abs_value

	a_queue.enqueue(copy.deepcopy(grid))

	return overflow(grid, a_queue) + 1
