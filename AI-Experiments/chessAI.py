import chess

# Evaluation function
def evaluate_board(board): 
    # A simple evaluation function that calculates the material value of the board.
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0  # King has no value as it's not capturable
    }

    evaluation = 0
    for piece in chess.PIECE_TYPES:
        evaluation += len(board.pieces(piece, chess.WHITE)) * piece_values[piece]
        evaluation -= len(board.pieces(piece, chess.BLACK)) * piece_values[piece]

    return evaluation

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    if maximizing_player:
        max_eval = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Function to find the best move
def find_best_move(board, depth):
    best_move = None
    max_eval = -float('inf')

    for move in board.legal_moves:
        board.push(move)
        board_eval = minimax(board, depth - 1, -float('inf'), float('inf'), False)
        board.pop()

        if board_eval > max_eval:
            max_eval = board_eval
            best_move = move

    return best_move

# Main game loop
def play_game():
    board = chess.Board()

    while not board.is_game_over():
        print(board)

        if board.turn == chess.WHITE:
            # Human player's move (White)
            print("\nYour possible moves are: ")
            print(", ".join([str(move) for move in board.legal_moves]))

            move = input("Enter your move: ")
            try:
                board.push_san(move)
            except ValueError:
                print("Invalid move. Please try again.")
        else:
            # AI player's move (Black)
            print("AI is thinking...")
            best_move = find_best_move(board, depth=3)  # You can adjust the depth for better AI
            board.push(best_move)
            print(f"AI plays: {best_move}")

    print("Game Over!")
    print(f"Result: {board.result()}")

if __name__ == "__main__":
    play_game()
