#https://www.hackerrank.com/challenges/botclean
# Head ends here
def next_move(posx, posy, board):
  locm = [posx, posy]
	#path = []
	for row in board[locm[0]:]:
		moveToRow = False
		while 'd' in row:
			if not moveToRow and locm[0] < board.index(row):
				locm[0] += 1
				moveToRow = True
				print 'DOWN'
				return
			locp = row.index('d')
			while locm[1] < locp:
				#path.append('RIGHT')
				locm[1] += 1
				print 'RIGHT'
				return
			while locm[1] > locp:
				#path.append('LEFT')
				locm[1] += 1
				print 'LEFT'
				return
			while locm[1] == locp:
				#path.append('CLEAN')
				board[locm[0]][locm[1]] = '-'
				print 'CLEAN'
				return
				
	for row in board[0:locm[0]:-1]:
		moveToRow = False
		while 'd' in row:
			if not moveToRow and locm[0] > board.index(row):
				locm[0] -= 1
				moveToRow = True
				print 'UP'
				return
			locp = row.index('d')
			while locm[1] < locp:
				#path.append('RIGHT')
				locm[1] += 1
				print 'RIGHT'
				return
			while locm[1] > locp:
				#path.append('LEFT')
				locm[1] += 1
				print 'LEFT'
				return
			while locm[1] == locp:
				#path.append('CLEAN')
				board[locm[0]][locm[1]] = '-'
				print 'CLEAN'
				return

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
