logo = """
_________                                     __       _____  
\_   ___ \  ____   ____   ____   ____   _____/  |_    /  |  | 
/    \  \/ /  _ \ /    \ /    \_/ __ \_/ ___\   __\  /   |  |_
\     \___(  <_> )   |  \   |  \  ___/\  \___|  |   /    ^   /
 \______  /\____/|___|  /___|  /\___  >\___  >__|   \____   | 
        \/            \/     \/     \/     \/            |__| 
"""

# Create a board with x size 7 and y size 6
def create_board(a, b):
    tempdict = {0: {0: {" "}}}
    templist = []
    for x in range(a):
        templist = {}
        for i in range(b):
            templist[i] = " "
        tempdict[x] = templist
    return tempdict

game_board = create_board(7, 6)
is_x_turn = True

def draw_board(board):
    for i in range(len(board[0])):
        for x in range(len(board)):
            print("|"+ str(board[x][i]), end="")
        print("|")
    print(" -|-|-|-|-|-|-")
    print(" 1 2 3 4 5 6 7")

def make_choice():
    global is_x_turn
    if is_x_turn:
        var = "x"
        is_x_turn = False
    else:
        var = "o"
        is_x_turn = True
    while True:
        choice = input("Pick a column 1 - 7: ")
        if not choice:
            return False
        elif not choice.isnumeric():
            print("Invalid input")
            return False
        elif int(choice) <= 7 and int(choice) >= 1:
            choice = int(choice) - 1
            for row in game_board:
                if int(row) == choice:
                    for column in game_board[row]:
                        t = [5, 4, 3, 2, 1, 0]
                        column = t[column]
                        if game_board[row][column] == " ":
                            game_board[row][column] = var
                            return (row, column)
                        
def find_neighbours(board, index):
    ix = index[0]
    iy = index[1]
    Neighbours = []

    if board[ix][iy]:
        for i in range(-1, 2):
            for x in range(-1, 2):
                if ix + i >= 0 and iy + x >= 0 and ix + i <= 6 and iy + x <= 5:
                    values = (ix + i, iy + x)
                    Neighbours.append(values)
    return Neighbours

def check_board(board, origin):
    x = origin[0]
    y = origin[1]
    methods = {
                "diag_right": 
                    [[1, 1],[-1, -1]], 
               "diag_left": 
                    [[1, -1],[-1, 1]], 
               "vertical": 
                    [[0, 1],[0, -1]],
                "horizontal": 
                    [[1, 0], [-1, 0]]
                }
    
    pointer1 = [x, y]
    pointer2 = [x, y]
    if not is_x_turn:
        player = "x"
    else:
        player = "o"

    for method in methods:
        count = 1
        for _ in range(4):
            next_x = pointer1[0] + methods[method][0][0]
            next_y = pointer1[1] + methods[method][0][1]
            previous_x = pointer2[0] + methods[method][1][0]
            previous_y = pointer2[1] + methods[method][1][1]

            if (0 <= next_x <= 6) and (0 <= next_y <= 5) and board[next_x][next_y] == player:
                count += 1
                pointer1 = (next_x, next_y)

                print(count)
                if count >= 4:
                    return player
                
            if (0 <= previous_x <= 6) and (0 <= previous_y <= 5) and board[previous_x][previous_y] == player:
                count += 1
                pointer2 = (next_x, next_y)
                
                print(count)
                if count >= 4:
                    return player
                
winner = ""        

print(logo)

def read_rules():
    hear_rules = False

    while not hear_rules:
        inp = input("Welcome to Axel's connect 4 do you know how to play (y/n)? ")
        if inp.lower() in ['y', 'n']:
            print("\n")
            if inp.lower == 'y':
                hear_rules = True
            break
        else:
            print("Invalid input")

while True:
    draw_board(game_board)
    if winner != "":
        break
    origin = make_choice()
    if origin:
        neighbours = find_neighbours(game_board, origin)
        if check_board(game_board, origin):
            winner = check_board(game_board, origin)

print("Player: "+ winner.upper() +" Wins")
