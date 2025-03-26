import random

# Step 1: Board banate hain (9 spaces wala list)
board = [" " for _ in range(9)]

# Step 2: Board print karne ka function
def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Step 3: Check karna ke koi jeeta to nahi
def check_winner(board, player):
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Step 4: AI (O) ka **Minimax Algorithm**
def minimax(board, is_maximizing):
    # Check karo AI ya player jeet gaya?
    if check_winner(board, "O"): return 1  # AI jeet gaya
    if check_winner(board, "X"): return -1  # Player jeet gaya
    if " " not in board: return 0  # Draw ho gaya

    if is_maximizing:  # AI ka move
        best_score = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:  # Player ka move
        best_score = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Step 5: AI ka move (sabse best move lega)
def ai_move():
    best_score = -float("inf")
    best_move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"

# Step 6: Player ka move
def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = "X"
                break
        print("Invalid move! Try again.")

# Step 7: Game Loop
def play_game():
    print("Welcome to Unbeatable Tic-Tac-Toe!")
    print_board()
    
    while True:
        player_move()  # Player ki turn
        print_board()
        if check_winner(board, "X"):
            print("🎉 You win! (somehow)")
            break
        if " " not in board:
            print("😐 It's a draw!")
            break
        
        print("AI's turn...")
        ai_move()  # AI ki turn
        print_board()
        if check_winner(board, "O"):
            print("💀 AI wins! Better luck next time.")
            break
        if " " not in board:
            print("😐 It's a draw!")
            break

# Step 8: Game ko run karo
play_game()
