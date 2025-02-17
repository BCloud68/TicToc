import random

# Display the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check if someone has won
def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if the board is full
def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

# AI chooses the best move
def ai_move(board):
    # Check if AI can win
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if check_winner(board, "O"):
                    return
                board[i][j] = " "

    # Block the player from winning
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if check_winner(board, "X"):
                    board[i][j] = "O"
                    return
                board[i][j] = " "

    # Random move (fallback)
    while True:
        i, j = random.randint(0, 2), random.randint(0, 2)
        if board[i][j] == " ":
            board[i][j] = "O"
            return

# Main game loop
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Player's turn
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] != " ":
                print("Cell already occupied! Try again.")
                continue
            board[row][col] = "X"
        except (ValueError, IndexError):
            print("Invalid move! Please enter a number between 1 and 9.")
            continue

        print("\nYour move:")
        print_board(board)

        # Check if player won
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break

        # Check for a draw
        if is_full(board):
            print("It's a draw!")
            break

        # AI's turn
        ai_move(board)
        print("\nAI's move:")
        print_board(board)

        # Check if AI won
        if check_winner(board, "O"):
            print("AI wins! Better luck next time.")
            break

        # Check for a draw
        if is_full(board):
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
