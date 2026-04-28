import math
WINS =[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def show_board(b):
    p =[b[i] if b[i] != ' ' else str(i+1)for i in range(9)]
    print(f"\n {p[0]} | {p[1]} | {p[2]} ")
    print("---+---+---")
    print(f" {p[3]} | {p[4]} | {p[5]} ")
    print("---+---+---")
    print(f" {p[6]} | {p[7]} | {p[8]} \n")


def checkwin(b,p):
    return any(b[a1]==b[a2]==b[a3]==p for a1,a2,a3 in WINS)

def is_full(b):
    return ' 'not in b

def minmax(b,depth,is_ai):
    if checkwin(b,'O'):
        return 10 - depth
    if checkwin(b,'X'):
        return depth -10
    if is_full(b):
        return 0
    moves =[i for i,c in enumerate(b) if c==' ']

    if is_ai:
        best = -math.inf
        for m in moves:
            b[m] ='O'
            best =max(best,minmax(b,depth+1,False))
            b[m] =' '
        return best
    else:
        best = math.inf
        for m in moves:
            b[m] = 'X'
            best = min(best,minmax(b,depth+1,True))
            b[m] = ' '
        return best
    
def ai_move(b):
    best,pick = -math.inf,None
    for i,c in enumerate(b):
        if c != ' ':
            continue
        b[i] ='O'
        score = minmax(b,0,False)
        b[i] =' '
        if score > best:
            best,pick = score,i
    return pick

def get_player_move(b):
    while True:
            pos = int(input("Your move: "))-1
            if 0<=pos<=8 and b[pos] ==' ':
                return pos
            print("that cell is taken")

def play():
    board=[' ']*9
    turn ='X'
    show_board(board)

    while True:
        if turn =='X':
            pos = get_player_move(board)
            board[pos] = 'X'
            show_board(board)
            if checkwin(board,'X'):
                print("you win")
            if is_full(board):
                print("draw")
                return
            turn ='O'
        else:
            print("ai is thinking..")
            m =ai_move(board)
            board[m] = 'O'
            print(f"ai played {m+1}")
            show_board(board)
            if checkwin(board,'O'):
                print("ai wins")
                return
            if is_full(board):
                print("draw")
                return
            turn ='X'

play()