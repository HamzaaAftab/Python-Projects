# Step 1: Create the board
def create_board():
    return [" "] * 9  # A list with 9 empty spaces representing the Tic-Tac-Toe grid

# Step 2: Display the board
def display_board(board):
    print("\n")  # Print a new line for spacing
    print(f" {board[0]} | {board[1]} | {board[2]} ")  # Top row
    print("---+---+---")  # Row separator
    print(f" {board[3]} | {board[4]} | {board[5]} ")  # Middle row
    print("---+---+---")  # Row separator
    print(f" {board[6]} | {board[7]} | {board[8]} ")  # Bottom row
    print("\n")  # Print a new line for spacing

# Step 3: Check if a player has won
def check_winner(board, player):
    # Define all possible winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    # Check if any winning combination has all three positions filled by the same player
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True  # Player wins
    return False  # No winner yet

# Step 4: Check if the board is full (Game Draw)
def is_draw(board):
    return " " not in board  # If no empty space is left, it's a draw

# Step 5: Get player input
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1  # Convert 1-9 to 0-8 index
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = player  # Place the player's symbol (X or O)
                break  # Exit loop after a valid move
            else:
                print("Invalid move. Try again!")  # If the spot is already taken
        except ValueError:
            print("Please enter a number between 1 and 9.")  # If the input is not a number

# Step 6: The game loop
def play_game():
    board = create_board()  # Create an empty board
    current_player = "X"  # X always starts first

    while True:
        display_board(board)  # Show the board
        player_move(board, current_player)  # Get the player's move

        if check_winner(board, current_player):  # Check if the player won
            display_board(board)
            print(f"🎉 Player {current_player} wins! 🎉")
            break  # End the game

        if is_draw(board):  # Check if the board is full (draw)
            display_board(board)
            print("It's a draw! 🤝")
            break  # End the game

        # Switch turns between players X and O
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    play_game()
