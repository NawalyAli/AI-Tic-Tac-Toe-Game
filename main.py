def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

board = create_board()
print_board(board)

def player_move(board, row, col, player):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False

def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

def evaluate(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return 10 if row[0] == 'X' else -10

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return 10 if board[0][col] == 'X' else -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return 10 if board[0][0] == 'X' else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return 10 if board[0][2] == 'X' else -10

    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth

    if not is_moves_left(board):
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best

def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def check_win(board):
    # Check rows, columns and diagonals for a win
    if evaluate(board) != 0:
        return True
    # Check if there are no more moves
    if not is_moves_left(board):
        return True
    return False

def main():
    board = create_board()
    player = 'O'  # Player starts with 'O'
    while True:
        print_board(board)
        if player == 'O':
            row, col = map(int, input("Enter your move (row and column): ").split())
            if not player_move(board, row, col, player):
                print("Invalid move, try again.")
                continue
        else:
            print("AI's turn...")
            row, col = find_best_move(board)
            player_move(board, row, col, player)

        if check_win(board):
            print_board(board)
            print(f"Player {player} wins!" if evaluate(board) != 0 else "It's a draw!")
            break

        player = 'X' if player == 'O' else 'O'

if __name__ == "__main__":
    main()
