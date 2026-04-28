import math

# All 8 possible winning combinations on a 3x3 board (indices 0 to 8)
WINS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    (0, 4, 8), (2, 4, 6)               # Diagonals
]

def show_board(b):
    """
    Prints the Tic-Tac-Toe board.
    Shows the cell number (1-9) if it is empty, or the player's symbol ('X' or 'O').
    """
    p = [b[i] if b[i] != ' ' else str(i + 1) for i in range(9)]
    print(f"\n {p[0]} | {p[1]} | {p[2]} ")
    print("---+---+---")
    print(f" {p[3]} | {p[4]} | {p[5]} ")
    print("---+---+---")
    print(f" {p[6]} | {p[7]} | {p[8]} \n")

def checkwin(b, p):
    """
    Checks if player 'p' ('X' or 'O') has won the game.
    """
    return any(b[a1] == b[a2] == b[a3] == p for a1, a2, a3 in WINS)

def is_full(b):
    """
    Checks if the board is completely full (resulting in a tie if no one won).
    """
    return ' ' not in b

def minmax(b, depth, is_ai):
    """
    The Minimax algorithm. It recursively simulates all possible future moves
    to find the optimal score for the current board state.
    """
    # 1. Base Cases: Return a score if the simulated game has ended
    if checkwin(b, 'O'):
        return 10 - depth  # AI wins (favours quicker wins)
    if checkwin(b, 'X'):
        return depth - 10  # Human wins (favours drawing out the loss)
    if is_full(b):
        return 0           # Draw

    # Find all available empty spaces on the board
    moves = [i for i, c in enumerate(b) if c == ' ']

    # 2. Recursive Cases
    if is_ai:
        # AI's turn: Aim to maximize the score
        best = -math.inf
        for m in moves:
            b[m] = 'O'  # Simulate the move
            best = max(best, minmax(b, depth + 1, False))
            b[m] = ' '  # Undo the move (backtrack)
        return best
    else:
        # Human's turn: Aim to minimize the score
        best = math.inf
        for m in moves:
            b[m] = 'X'  # Simulate the move
            best = min(best, minmax(b, depth + 1, True))
            b[m] = ' '  # Undo the move (backtrack)
        return best

def ai_move(b):
    """
    Evaluates all available moves for the AI using Minimax 
    and returns the index of the best possible move.
    """
    best = -math.inf
    pick = None
    
    # Loop through all spaces on the board
    for i, c in enumerate(b):
        if c != ' ':
            continue  # Skip taken spaces
            
        b[i] = 'O'              # Simulate AI move
        score = minmax(b, 0, False) # Evaluate move with Minimax
        b[i] = ' '              # Undo simulated move
        
        # If this move yields a better score than before, record it
        if score > best:
            best = score
            pick = i
            
    return pick

def get_player_move(b):
    """
    Asks the human player for a move and validates the input.
    """
    while True:
        try:
            # Convert 1-9 input to 0-8 list index
            pos = int(input("Your move (1-9): ")) - 1
            if 0 <= pos <= 8 and b[pos] == ' ':
                return pos
            print("That cell is taken or invalid!")
        except ValueError:
            print("Please enter a valid number between 1 and 9.")

def play():
    """
    The main driver function that runs the game loop.
    """
    board = [' '] * 9  # Initialize empty 3x3 board
    turn = 'X'         # Human ('X') starts first
    
    show_board(board)
    
    while True:
        if turn == 'X':
            # Human Player Turn
            pos = get_player_move(board)
            board[pos] = 'X'
            show_board(board)
            
            # Check Human victory or draw
            if checkwin(board, 'X'):
                print("You win!")
                return
            if is_full(board):
                print("It's a draw!")
                return
                
            turn = 'O' # Pass turn to AI
            
        else:
            # AI Player Turn
            print("AI is thinking...")
            m = ai_move(board)
            board[m] = 'O'
            print(f"AI played cell {m + 1}")
            show_board(board)
            
            # Check AI victory or draw
            if checkwin(board, 'O'):
                print("AI wins!")
                return
            if is_full(board):
                print("It's a draw!")
                return
                
            turn = 'X' # Pass turn to Human

# Start the game
if __name__ == "__main__":
    play()
