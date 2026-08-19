# Tic-Tac-Toe AI using Minimax Algorithm
# Human Player: X
# AI Player: O


# Function to display the Tic-Tac-Toe board
def print_board(board):
    print()

    # Display the board in 3 rows
    for i in range(3):
        print(" | ".join(board[i * 3:(i + 1) * 3]))

        # Print separator between rows
        if i < 2:
            print("-" * 9)

    print()


# Function to check whether there is a winner or a draw
def check_winner(board):

    # All possible winning combinations
    winning_combinations = [
        (0, 1, 2),  # First row
        (3, 4, 5),  # Second row
        (6, 7, 8),  # Third row
        (0, 3, 6),  # First column
        (1, 4, 7),  # Second column
        (2, 5, 8),  # Third column
        (0, 4, 8),  # Main diagonal
        (2, 4, 6)   # Other diagonal
    ]

    # Check all winning combinations
    for a, b, c in winning_combinations:

        # If the three positions contain the same player
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    # If there are no empty spaces, the game is a draw
    if " " not in board:
        return "Draw"

    # Game is still in progress
    return None


# Minimax algorithm to find the best move for the AI
def minimax(board, is_maximizing):

    # Check the current state of the game
    result = check_winner(board)

    # AI wins
    if result == "O":
        return 1

    # Human player wins
    elif result == "X":
        return -1

    # Draw
    elif result == "Draw":
        return 0

    # AI's turn - AI tries to maximize the score
    if is_maximizing:
        best_score = -float("inf")

        # Try every empty position
        for i in range(9):
            if board[i] == " ":

                # Make a temporary AI move
                board[i] = "O"

                # Recursively calculate the score
                score = minimax(board, False)

                # Undo the temporary move
                board[i] = " "

                # Select the highest score
                best_score = max(best_score, score)

        return best_score

    # Human player's turn - AI assumes the human minimizes the score
    else:
        best_score = float("inf")

        # Try every empty position
        for i in range(9):
            if board[i] == " ":

                # Make a temporary human move
                board[i] = "X"

                # Recursively calculate the score
                score = minimax(board, True)

                # Undo the temporary move
                board[i] = " "

                # Select the lowest score
                best_score = min(best_score, score)

        return best_score


# Function to find the best move for the AI
def best_move(board):

    # Start with the lowest possible score
    best_score = -float("inf")

    # Store the best position
    move = None

    # Check every position on the board
    for i in range(9):

        # Only consider empty positions
        if board[i] == " ":

            # Temporarily place the AI's move
            board[i] = "O"

            # Calculate the score using Minimax
            score = minimax(board, False)

            # Undo the temporary move
            board[i] = " "

            # Update the best move if this move is better
            if score > best_score:
                best_score = score
                move = i

    return move


# Function to get a valid move from the player
def get_player_move(board):

    # Keep asking until the player enters a valid move
    while True:
        try:
            # Ask the player to enter a position
            position = int(input("Enter your move (1-9): "))

            # Check whether the number is between 1 and 9
            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
                continue

            # Convert the user's position to a list index
            index = position - 1

            # Check whether the selected position is already occupied
            if board[index] != " ":
                print("That position is already occupied. Choose another one.")
                continue

            # Return the valid position
            return index

        # Handle non-numeric input
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


# Main function to run the game
def main():

    # Create an empty Tic-Tac-Toe board
    board = [" "] * 9

    # Display the game instructions
    print("Welcome to Tic-Tac-Toe!")
    print("You are X and the AI is O.")
    print("Enter a number from 1 to 9 to make your move.")

    # Continue the game until someone wins or it ends in a draw
    while True:

        # Display the current board
        print_board(board)

        # Get the human player's move
        player_move = get_player_move(board)

        # Place X on the selected position
        board[player_move] = "X"

        # Check the result after the player's move
        result = check_winner(board)

        # If the game has ended
        if result:
            print_board(board)

            if result == "X":
                print("Congratulations! You win!")
            else:
                print("It's a draw!")

            break

        # AI's turn
        print("AI is thinking...")

        # Find the best move using Minimax
        ai_move = best_move(board)

        # Place O on the best position
        if ai_move is not None:
            board[ai_move] = "O"

        # Check the result after the AI's move
        result = check_winner(board)

        # If the game has ended
        if result:
            print_board(board)

            if result == "O":
                print("AI wins!")
            else:
                print("It's a draw!")

            break


# Start the game
# This ensures main() runs only when this file is executed directly
if __name__ == "__main__":
    main()