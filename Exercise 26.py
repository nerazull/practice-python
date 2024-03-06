# This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1, Part 3, and Part 4.

# As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

# If a game of Tic Tac Toe is represented as a list of lists, like so:

# game = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. 
# A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.

# Here are some more examples to work with:

# winner_is_2 = [[2, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]

# winner_is_1 = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]

# winner_is_also_1 = [[0, 1, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]

# no_winner = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 2]]

# also_no_winner = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 0]]

ttt_board = [[1, 1, 0],
             [2, 1, 2],
             [2, 0, 1]]

# Solution 2 from website; read, understood and slightly adjusted (it only returned the values 1 or 2 instead of printing, and the diag conditions were incorrect since and operator takes precedence over or, so a 2-2-2 diagonal could print as Player 1 won)
# My solution for which I am ashamed is after, I was getting frustrated at not coming up with something else and wanted to have something working before checking solutions
def checkGrid(grid):
	# rows
	for x in range(0,3):
		row = set([grid[x][0],grid[x][1],grid[x][2]])
		if len(row) == 1 and grid[x][0] == 1:
			print('Player 1 won')
		elif len(row) == 1 and grid[x][0] == 2:
			print('Player 2 won')
		
	for x in range(3):
		column = set([grid[0][x],grid[1][x],grid[2][x]])
		if len(column) == 1 and grid[0][x] == 1:
			print('Player 1 won')
		elif len(column) == 1 and grid[0][x] == 2:
			print('Player 2 won')
		
	diag1 = set([grid[0][0],grid[1][1],grid[2][2]])
	diag2 = set([grid[0][2],grid[1][1],grid[2][0]])
	if (len(diag1) == 1 or len(diag2) == 1) and grid[1][1] == 1:
		print('Player 1 won')
	elif (len(diag1) == 1 or len(diag2) == 1) and grid[1][1] == 2:
		print('Player 2 won')

checkGrid(ttt_board)

############## My initial solution, so I could allow myself to check for actual solutions
# if ttt_board[0] == [1, 1, 1] or ttt_board[1] == [1, 1, 1] or ttt_board[2] == [1, 1, 1]:
#     print('Player 1 wins')
# if ttt_board[0] == [2, 2, 2] or ttt_board[1] == [2, 2, 2] or ttt_board[2] == [2, 2, 2]:
#     print('Player 2 wins')

# column1 = []
# column2 = []
# column3 = []

# for elem in ttt_board:
#     columns = 0
#     column1.append(elem[columns])
#     columns += 1
#     column2.append(elem[columns])
#     columns += 1
#     column3.append(elem[columns])

# if column1[0] == column1[1] == column1[2] == 1:
#     print('Player 1 wins')
# elif column1[0] == column1[1] == column1[2] == 2:
#     print('Player 2 wins')

# if column2[0] == column2[1] == column2[2] == 1:
#     print('Player 1 wins')
# elif column2[0] == column2[1] == column2[2] == 2:
#     print('Player 2 wins')

# if column3[0] == column3[1] == column3[2] == 1:
#     print('Player 1 wins')
# elif column3[0] == column3[1] == column3[2] == 2:
#     print('Player 2 wins')    

# if ttt_board[0][0] == ttt_board[1][1] == ttt_board [2][2] == 1:
#     print('Player 1 wins')
# if ttt_board[0][0] == ttt_board[1][1] == ttt_board [2][2] == 2:
#     print('Player 2 wins')

# if ttt_board[0][2] == ttt_board[1][1] == ttt_board [2][0] == 1:
#     print('Player 1 wins')
# if ttt_board[0][2] == ttt_board[1][1] == ttt_board [2][2] == 2:
#     print('Player 2 wins')
