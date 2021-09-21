import pygame
import sudoku_solver as ss


def main():
    board, original, solution = get_board()
    gameWindow, myfont = initilize_game(board)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(gameWindow,(pos[0]//50, pos[1]//50),myfont,original,board)
            if event.type == pygame.KEYDOWN:
                if event.key == 107 or event.key == 75:
                    check(solution,original,board,gameWindow,myfont)
                if event.key == 115 or event.key == 83:
                    show_solution(gameWindow,myfont,solution,original,board)
                if event.key == 114 or event.key == 82:
                    board = [[original[x][y] for y in range(len(original[0]))] for x in range(len(original))]
                    gameWindow.fill((250,235,215))
                    draw_table(board,gameWindow,myfont)
                    pygame.display.update()
            if event.type == pygame.QUIT:
                pygame.quit()
                return

def get_board():
    """board = [
        [1,4,3,7,0,8,9,0,0],
        [0,9,5,0,0,0,1,0,0],
        [0,7,2,0,5,9,0,4,0],
        [4,8,9,6,1,7,0,5,0],
        [0,2,6,9,8,0,0,1,0],
        [7,0,0,3,0,0,6,0,0],
        [0,3,0,2,0,0,0,6,0],
        [5,6,0,0,9,0,0,0,4],
        [0,0,4,0,0,0,7,8,9]
    ]"""
    difficulty = "easy"
    #difficulty = "medium"
    #difficulty = "hard"
    board = ss.generate_board(difficulty)
    original = [[board[x][y] for y in range(len(board[0]))] for x in range(len(board))]
    solution = [[board[x][y] for y in range(len(board[0]))] for x in range(len(board))]
    ss.solve(solution)
    return board, original, solution

def initilize_game(board):
    pygame.init()
    gameWindow = pygame.display.set_mode((550,550))
    pygame.display.set_caption("Sudoku")
    gameWindow.fill((250,235,215))
    pygame.font.init()
    myfont = pygame.font.SysFont('Ariel',35)
    draw_table(board,gameWindow,myfont)
    return gameWindow, myfont

def draw_table(bd,window,font):
    for i in range(0,10):
        if i%3 == 0:
            pygame.draw.line(window, (0,0,0), (50 + 50*i, 50), (50 + 50*i,500),3)
            pygame.draw.line(window, (0,0,0), (50, 50 + 50*i),(500, 50 +50*i),3)
        else:
            pygame.draw.line(window, (0,0,0), (50 + 50*i, 50), (50 + 50*i,500),1)
            pygame.draw.line(window, (0,0,0), (50, 50 + 50*i),(500, 50 +50*i),1)
    pygame.display.update()
    
    for i in range(len(bd)):
        for j in range(len(bd[i])):
            if bd[i][j] != 0:
                value = font.render(str(bd[i][j]),True,(0,0,0))
                window.blit(value,((j+1)*50 + 15, (i+1)*50 + 15))
    pygame.display.update()
    pass

def insert(window,pos,font,board_original,board):
    i,j = pos[1],pos[0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if (board_original[i-1][j-1]!= 0):
                    return
                if event.key == 8:
                    board[i-1][j-1] = 0
                    pygame.draw.rect(window,(250,235,215),(pos[0]*50 + 5, pos[1]*50 + 5,50 -2*5,50-2*5))
                    pygame.display.update()
                    return

                if (48 < event.key < 58):
                    pygame.draw.rect(window,(250,235,215),(pos[0]*50 + 5, pos[1]*50 + 5,50 -2*5,50-2*5))
                    value = font.render(str(event.key-48),True,(0,0,255))
                    window.blit(value, (pos[0]*50 +15, pos[1]*50+15))
                    board[i-1][j-1] = event.key - 48
                    pygame.display.update()
                    return
                return

def check(solution, original,board,window,font):

    if solution == board:
        window.fill((0,255,0))
        draw_table(solution,window,font)
        pygame.display.update()
        return

    for i in range(len(board)):
        for j in range(len(board[i])):
            if original[i][j] == 0 and board[i][j] != 0:
                value = board[i][j]
                if value == solution[i][j]:
                    pygame.draw.rect(window,(250,235,215),((j+1)*50 + 5, (i+1)*50 + 5,50 -2*5,50-2*5))
                    value = font.render(str(value),True,(0,255,0))
                    window.blit(value,((j+1)*50 + 15, (i+1)*50 + 15))
                    pygame.display.update()
                else:
                    pygame.draw.rect(window,(250,235,215),((j+1)*50 + 5, (i+1)*50 + 5,50 -2*5,50-2*5))
                    value = font.render(str(value),True,(255,0,0))
                    window.blit(value,((j+1)*50 + 15, (i+1)*50 + 15))
                    pygame.display.update()                  
        
def show_solution(window,font,solution,original,board):
    for i in range(len(solution)):
        for j in range(len(solution[i])):
            if original[i][j] == 0:
                value = solution[i][j]
                board[i][j] = value
                pygame.draw.rect(window,(250,235,215),((j+1)*50 + 5, (i+1)*50 + 5,50 -2*5,50-2*5))
                value = font.render(str(value),True,(0,0,255))
                window.blit(value,((j+1)*50 + 15, (i+1)*50 + 15))
                pygame.display.update()

main()
