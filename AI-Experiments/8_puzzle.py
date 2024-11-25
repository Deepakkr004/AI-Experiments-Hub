import heapq

def manhattan(board):
    distance = 0
    for i in range(9):
        if board[i] != 0:
            x, y = divmod(i, 3)
            gx, gy = divmod(board[i] - 1, 3)
            distance += abs(x - gx) + abs(y - gy)
    return distance

def solve_puzzle(start_board):
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    start_state = (manhattan(start_board), 0, start_board.index(0), start_board, [])
    open_list = [start_state]
    closed_set = set()

    while open_list:
        _, g, blank_pos, board, path = heapq.heappop(open_list)
        if board == list(range(1, 9)) + [0]:
            return path + [board]
        closed_set.add(tuple(board))
        x, y = divmod(blank_pos, 3)

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_blank_pos = nx * 3 + ny
                new_board = board[:]
                new_board[blank_pos], new_board[new_blank_pos] = new_board[new_blank_pos], new_board[blank_pos]
                new_state = (g + 1 + manhattan(new_board), g + 1, new_blank_pos, new_board, path + [board])
                if tuple(new_board) not in closed_set:
                    heapq.heappush(open_list, new_state)

    return None

def print_solution(solution):
    for step in solution:
        print('\n'.join([' '.join(map(str, step[i:i+3])) for i in range(0, 9, 3)]))
        print()

# Example usage:
start_board = [1, 2, 3, 4, 5, 6, 0, 7, 8]
solution = solve_puzzle(start_board)

if solution:
    print("Solution found!")
    print_solution(solution)
else:
    print("No solution exists.")
