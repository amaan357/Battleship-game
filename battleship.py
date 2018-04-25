from random import randint

board = []
size = 0
while size == 0:
    size = int(input("Enter size of Board:(min 5,max 9) "))
    if size not in range(5,10):
        size = 0
for x in range(size):
    board.append(["O"] * size)

def print_board(board):
    for row in board:
        print(" ".join(row))

print("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = []
ship_col = []
ship_row.append(random_row(board))
ship_col.append(random_row(board))
times = 0
while times < size-5:
    row = random_row(board)
    col = random_col(board)
    if not all([ship_row[x]==row and ship_col[x]==col for x in range(times+1)]):
        ship_row.append(row)
        ship_col.append(col)
        times += 1
y = 0
print("You have total "+str(size-1)+" turns")
for turn in range(size-1):
    print("Turn"), turn + 1
    guess_row = int(input("Guess Row:")) - 1
    guess_col = int(input("Guess Col:")) - 1

    if all([guess_row == ship_row[x] and guess_col == ship_col[x] for x in range(size-4)]):
        print("Congratulations! You sunk my battleship!")
        board[guess_row][guess_col] = "H"
        y +=1
        if y == size-3:
            print("Congratulations! You sunk all my battleships!")
            break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "H"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            print_board(board)
        if turn == 3:
            print("Game Over")
