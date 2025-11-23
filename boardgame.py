#boardvisuals
from game2dboard import Board
from collection import Counter

EMPTY = None
BLACK = "⚫"
WHITE = "⚪"
current = BLACK
total = 64


def mouse_fn(btn, row, col):    
    global current, total
    if b[row][col] is not None:
        b.title = "That tile is already taken!"
        return
    
    b[row][col] = current
    current = WHITE if current == BLACK else BLACK
    b.title = f"Othello! Turn: {'Black ⚫' if current == BLACK else 'White ⚪'}"

b = Board(8,8)         
b[3][3] = WHITE
b[4][3] = BLACK
b[3][4] = BLACK
b[4][4] = WHITE


b.title = "Othello!  Turn: Black ⚫"
b.cell_size = 40       
b.cell_color = "green"
b.on_mouse_click = mouse_fn
b.show()
  
#How do you call a fish wearing a bowtie?
#Sofishticated :D :D :D


def pointcounter(counter: int, move):
    white = 0 #pointcounter for white
    black = 0 # pointcounter for black
    row = len(b)
    col = len(b[0])
    if is mouse_fn(move) and is flip(move): #if the move and the flip is done so I call it on the move variable, the counter starts to add up the received points to the pointcounters
        #now I handle the board as a matrix so I iterate over it
        for i in range(row):
            for j in range(col):
                if b[i][j] == WHITE: #here if the function finds a white piece, adds one to white's counter
                    white += 1
                    print("White: ", white) #I decided on printing the points, so players can check during game, since I assume it updates during the game, I mean the point counter
                elif b[i][j] == BLACK: #here if finds black, adds 1 to black's counter
                    black += 1
                    print("Black: ", black)
                else:
                    continue #otherwise continue to the next iteration

    def wincounter(gamesplayed, ww, wb):
        ww = 0
        wb = 0
        if possible_move is None or Empty is None: #there is no possible move to be made or no empty space left
            if white>black: #checking if white has more points
                ww+=1 #add one win to white
            elif white<black: #same thing but for black
                wb+=1
            elif white == black: #if it is a tie both receive half a point, yeah well this is just my thing from chess, but idk how is it in othello
                ww += 0.5
                wb += 0.5
            else:
                print("Game is unconclusive")
            return ww, wb #here i just return the wins
    

    return white, black #yeah and just here I return the points in one game for both colors

    
    
