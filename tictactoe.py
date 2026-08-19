# Tic-Tac-Toe AI using Minimax Algorithm
# The AI (O) plays against the Human (X) and never loses.
# Minimax works by simulating every possible future move,
# then picking the move that gives the best outcome for the AI.

# The board is a list of 9 items representing positions 0-8:
# 0 | 1 | 2
# 3 | 4 | 5
# 6 | 7 | 8

board = [" " for _ in range(9)]  # Empty board to start


def print_board():
    # Prints the board in a readable 3x3 grid
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("---------")


def check_winner(b, player):
    # All possible winning combinations (rows, columns, diagonals)
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(b[i] == player for i in condition):
            return True
    return False


def is_board_full(b):
    # Returns True if there are no empty spaces left
    return " " not in b


def minimax(b, depth, is_maximizing):
    # This function recursively evaluates all possible moves
    # and returns a score: +1 if AI (O) wins, -1 if Human (X) wins, 0 if draw

    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if is_board_full(b):
        return 0

    if is_maximizing:
        # AI's turn - trying to get the highest score
        best_score = -float("inf")
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, False)
                b[i] = " "  # undo move (backtrack)
                best_score = max(score, best_score)
        return best_score
    else:
        # Human's turn - assume they play their best move too
        best_score = float("inf")
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, True)
                b[i] = " "  # undo move (backtrack)
                best_score = min(score, best_score)
        return best_score


def best_move():
    # Finds the best possible move for the AI using minimax
    best_score = -float("inf")
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "  # undo move
            if score > best_score:
                best_score = score
                move = i
    return move


def main():
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print("Positions are numbered 0-8, left to right, top to bottom.")
    print_board()

    while True:
        # Human move
        human_move = int(input("Enter your move (0-8): "))
        if board[human_move] != " ":
            print("That spot is taken! Try again.")
            continue
        board[human_move] = "X"

        if check_winner(board, "X"):
            print_board()
            print("You win!")
            break
        if is_board_full(board):
            print_board()
            print("It's a draw!")
            break

        # AI move
        ai_move = best_move()
        board[ai_move] = "O"
        print(f"AI played position {ai_move}")
        print_board()

        if check_winner(board, "O"):
            print("AI wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()