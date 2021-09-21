import requests

def display(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(str(board[i][j]))
            else:
                print(str(board[i][j]) + " ",end="")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i,j)

def valid(board,value,pos):
    #check row
    for j in range(len(board[pos[0]])):
        if value == board[pos[0]][j]:
            return False
    #check column
    for i in range(len(board)):
        if value == board[i][pos[1]]:
            return False
    #check box
    box_y = pos[0]//3
    box_x = pos[1]//3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if value == board[i][j]: 
                return False
    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, pos = find

    for i in range(1,10):
        if valid(board,i,find):
            board[row][pos] = i
            
            if solve(board):
                return True
            
            board[row][pos] = 0

    return False

def generate_board(difficulty):
    easy = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
    medium = requests.get("https://sugoku.herokuapp.com/board?difficulty=medium")
    hard = requests.get("https://sugoku.herokuapp.com/board?difficulty=hard")
    if difficulty == "easy":
        board = easy.json()["board"]
    if difficulty == "medium":
        board = medium.json()["board"]
    if difficulty == "hard":
        board = hard.json()["board"]
    return board

