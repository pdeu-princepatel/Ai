import math

WINS = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def show_board(b):
    print()
    for r in range(3):
        row = b[r*3 : r*3+3]
        print("  " + " | ".join(c if c != ' ' else str(r*3+i+1) for i,c in enumerate(row)))
        if r < 2:
            print("  --+---+--")
    print()

def check_win(b, p):
    return any(b[a]==b[c2]==b[c3]==p for a,c2,c3 in WINS)

def is_full(b):
    return ' ' not in b

def minimax(b, depth, is_ai):
    if check_win(b, 'O'):
        return 10 - depth
    if check_win(b, 'X'):
        return depth - 10
    if is_full(b):
        return 0

    moves = [i for i,c in enumerate(b) if c == ' ']

    if is_ai:
        best = -math.inf
        for m in moves:
            b[m] = 'O'
            best = max(best, minimax(b, depth+1, False))
            b[m] = ' '
        return best
    else:
        best = math.inf
        for m in moves:
            b[m] = 'X'
            best = min(best, minimax(b, depth+1, True))
            b[m] = ' '
        return best

def ai_move(b):
    best, pick = -math.inf, None
    for i,c in enumerate(b):
        if c != ' ':
            continue
        b[i] = 'O'
        score = minimax(b, 0, False)
        b[i] = ' '
        if score > best:
            best, pick = score, i
    return pick

def get_player_move(b):
    while True:
        try:
            pos = int(input("your move (1-9): ")) - 1
            if 0 <= pos <= 8 and b[pos] == ' ':
                return pos
            print("that cell is taken or invalid, try again")
        except ValueError:
            print("enter a number from 1 to 9")

def play():
    board = [' '] * 9
    choice = input("go first? (y/n): ").strip().lower()
    human_first = choice != 'n'
    turn = 'X' if human_first else 'O'

    show_board(board)

    while True:
        if turn == 'X':
            pos = get_player_move(board)
            board[pos] = 'X'
            show_board(board)
            if check_win(board, 'X'):
                print("you win")
                return
            if is_full(board):
                print("draw")
                return
            turn = 'O'
        else:
            print("ai is thinking...")
            m = ai_move(board)
            board[m] = 'O'
            print(f"ai played {m+1}")
            show_board(board)
            if check_win(board, 'O'):
                print("ai wins")
                return
            if is_full(board):
                print("draw")
                return
            turn = 'X'

if __name__ == "__main__":
    while True:
        play()
        again = input("play again? (y/n): ").strip().lower()
        if again != 'y':
            break