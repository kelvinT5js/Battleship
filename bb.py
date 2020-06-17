from random import randint

reset = True
#while reset == True:
board = []
for i in range(10):
	board.append(["O"] * 10)


		
letters = {
1 : 'A', 
2 : 'B', 
3 : 'C',
4 : 'D',
5 : 'E',
6 : 'F',
7 : 'G',
8 : 'H',
9 : 'I',
10 : 'J'}


def print_board(board):
	print '  ',
	for i in range(1, 10):
		print ' ' + str(i),
	print '',
	print 10
	print '  ',
	for i in range(1, 10):
		print ' |',
	print '',
	print '|'
	count = 1
	for row in board:
		print letters[count] + ' -', '  '.join(row)
		count += 1
	
print_board(board)	

location = []
int_location = []

class Ship(object):
	
	def __init__(self, row, col, length):
		self.row = row
		self.col = col
		self.length = length
		self.cols = []

	def column(self):	
		for i in range(self.col, self.col + self.length):
			self.cols.append(i)
			if i > 10:
				self.cols.remove(i)
				self.cols.append(self.cols[0] - 1)
				self.cols.sort()
		return self.cols

	def spots(self):
		location = []
		int_location = []
		self.row = str(self.row)
		for i in self.cols:
			i = str(i)
			spot = str(self.row + i)
			location.append(spot)
	
		for i in location:
			beep = int(i)
			int_location.append(beep)

		return int_location

class Vertical_Ship(Ship):

	def spots(self):
		location = []
		int_location = []
		self.col = str(self.col)
		for i in self.cols:
			i = str(i)
			spot = str(i + self.col)
			location.append(spot)

		for i in location:
			beep = int(i)
			int_location.append(beep)

		return int_location



def ship_carrier():
	ship_carrier = []
	ship_row_carrier = randint(1, 10)
	ship_col_carrier = randint(1, 10)
	up_or_down_carrier = randint(1, 2)
	if up_or_down_carrier == 1:
		ship_carrier = Vertical_Ship(ship_row_carrier, ship_col_carrier, 5)
	else:
		ship_carrier = Ship(ship_row_carrier, ship_col_carrier, 5)
	ship_carrier.column()
	location_carrier = ship_carrier.spots()
	return location_carrier


def ship_battleship():
	ship_battleship = []
	ship_row_battleship = randint(1, 10)
	ship_col_battleship = randint(1, 10)
	up_or_down_battleship = randint(1, 2)
	if up_or_down_battleship == 1:
		ship_battleship = Vertical_Ship(ship_row_battleship, ship_col_battleship, 4)
	else:
		ship_battleship = Ship(ship_row_battleship, ship_col_battleship, 4)
	ship_battleship.column()
	location_battleship = ship_battleship.spots()
	return location_battleship

def ship_cruiser():
	ship_cruiser = []
	ship_row_cruiser = randint(1, 10)
	ship_col_cruiser = randint(1, 10)
	up_or_down_cruiser = randint(1, 2)
	if up_or_down_cruiser == 1:
		ship_cruiser = Vertical_Ship(ship_row_cruiser, ship_col_cruiser, 3)
	else:
		ship_cruiser = Ship(ship_row_cruiser, ship_col_cruiser, 3)
	ship_cruiser.column()
	location_cruiser = ship_cruiser.spots()
	return location_cruiser

def ship_submarine():
	ship_submarine = []
	ship_row_submarine = randint(1, 10)
	ship_col_submarine = randint(1, 10)
	up_or_down_submarine = randint(1, 2)
	if up_or_down_submarine == 1:
		ship_submarine = Vertical_Ship(ship_row_submarine, ship_col_submarine, 3)
	else:
		ship_submarine = Ship(ship_row_submarine, ship_col_submarine, 3)
	ship_submarine.column()
	location_submarine = ship_submarine.spots()
	return location_submarine

def ship_destroyer():
	ship_destroyer = []
	ship_row_destroyer = randint(1, 10)
	ship_col_destroyer = randint(1, 10)
	up_or_down_destroyer = randint(1, 2)
	if up_or_down_destroyer == 1:
		ship_destroyer = Vertical_Ship(ship_row_destroyer, ship_col_destroyer, 2)
	else:
		ship_destroyer = Ship(ship_row_destroyer, ship_col_destroyer, 2)
	ship_destroyer.column()
	location_destroyer = ship_destroyer.spots()
	return location_destroyer

int_location_carrier = ship_carrier()
print int_location_carrier

int_location_battleship = ship_battleship()
print int_location_battleship

int_location_cruiser = ship_cruiser()
print int_location_cruiser

int_location_submarine = ship_submarine()
print int_location_submarine

int_location_destroyer = ship_destroyer()
print int_location_destroyer


def checker(ship_1, ship_2, ship_3, ship_4, ship_5):
	checking = True
	while checking == True:
		checklist = []
		for i in ship_1:
			if i not in checklist:
				checklist.append(i)
		for i in ship_2:
			if i not in checklist:
				checklist.append(i)
		for i in ship_3:
			if i not in checklist:
				checklist.append(i)
		for i in ship_4:
			if i not in checklist:
				checklist.append(i)
		for i in ship_5:
			if i not in checklist:
				checklist.append(i)

		if len(checklist) == len(ship_1) + len(ship_2) + len(ship_3) + len(ship_4) + len(ship_5):
			print 'good'
			checking = False
			good = True
		else:
			print 'duplicates'
			checking = False
			good = False
			reset = True

	while good == True:
		print checklist
		int_location_carrier = ship_1
		int_location_battleship = ship_2
		int_location_cruiser = ship_3
		int_location_submarine = ship_4
		int_location_destroyer = ship_5

		return int_location_carrier
		return int_location_battleship
		return int_location_cruiser
		return int_location_submarine
		return int_location_destroyer

checker(int_location_carrier, int_location_battleship, int_location_cruiser, int_location_submarine, int_location_destroyer)


game_on = True
while game_on == True:
	guessing = True
	while guessing == True:
		input_row = raw_input("Guess a row: ")
		if input_row.isalpha():
			input_row = input_row.upper()
			for num, let in letters.items():
				if let == input_row:
					guess_row = num
					guessing = False
		else:
			print 'Try again . . . '
	
	while True:
		try:
			guess_col = int(raw_input("Guess a column: "))
			break
		except ValueError:
			print 'Try again . . .'



	guess_location = int(str(guess_row) + str(guess_col))

	if guess_location in int_location_carrier:
		board[guess_row - 1][guess_col - 1] = '#'
		print_board(board)
		print 'HIT'
		int_location_carrier.remove(guess_location)
	elif guess_location in int_location_battleship:
		board[guess_row - 1][guess_col - 1] = '#'
		print_board(board)
		print 'HIT'
		int_location_battleship.remove(guess_location)
	elif guess_location in int_location_cruiser:
		board[guess_row - 1][guess_col - 1] = '#'
		print_board(board)
		print 'HIT'
		int_location_cruiser.remove(guess_location)
	elif guess_location in int_location_submarine:
		board[guess_row - 1][guess_col - 1] = '#'
		print_board(board)
		print 'HIT'
		int_location_submarine.remove(guess_location)
	elif guess_location in int_location_destroyer:
		board[guess_row - 1][guess_col - 1] = '#'
		print_board(board)
		print 'HIT'
		int_location_destroyer.remove(guess_location)		
	elif guess_row  not in range(1, 11) or guess_col not in range(1, 11):
		print_board(board)
		print 'That\'s not even in the ocean'
	elif board[guess_row - 1][guess_col - 1] == 'X' or board[guess_row - 1][guess_col - 1] == '#':
		print_board(board)
		print 'You already guessed that'
	else:
		board[guess_row - 1][guess_col - 1] = 'X'
		print_board(board)
		print 'You Missed'
	
	if int_location_carrier == []:
		print 'You sunk the carrier!'
		int_location_carrier.append('empty')
	elif int_location_battleship == []:
		print 'You sunk the battleship!'
		int_location_battleship.append('empty')
	elif int_location_cruiser == []:
		print 'You sunk the cruiser!'
		int_location_cruiser.append('empty')
	elif int_location_submarine == []:
		print 'You sunk the submarine!'
		int_location_submarine.append('empty')
	elif int_location_destroyer == []:
		print 'You sunk the destroyer!'
		int_location_destroyer.append('empty')

	if int_location_carrier == ['empty'] and int_location_battleship == ['empty'] and int_location_cruiser == ['empty'] and int_location_submarine == ['empty'] and int_location_destroyer == ['empty']:
		print 'You sunk all the ships! YOU WIN!'
		break

	print int_location_carrier
	print int_location_battleship
	print int_location_cruiser
	print int_location_submarine
	print int_location_destroyer

	








