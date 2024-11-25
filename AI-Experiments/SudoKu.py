import pygame
 
# Initialize Pygame
pygame.init()
 
# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_BLUE = (173, 216, 230)
 
# Set up display
BOARD_SIZE = 9
CELL_SIZE = 60
MARGIN = 20
WIDTH = HEIGHT = BOARD_SIZE * CELL_SIZE + 2 * MARGIN
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive AI Sudoku Solver")
 
# Initialize font
font = pygame.font.Font(None, 40)
message_font = pygame.font.Font(None, 36)
win_font = pygame.font.Font(None, 48)  # Font for winning message
 
# Initial Sudoku puzzle with zeros as empty spaces
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
 
# Correct solution for the above puzzle
solution_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
 
# Track selected cell
selected_row, selected_col = None, None
message = ""
message_timer = 0
hint_timer = 0
hint_number = 0
game_won = False  # Track if the game is won
 
def draw_board():
    screen.fill(WHITE)
    
    # Draw grid lines
    for row in range(BOARD_SIZE + 1):
        line_width = 3 if row % 3 == 0 else 1
        pygame.draw.line(screen, BLACK, (MARGIN, MARGIN + row * CELL_SIZE), 
                         (WIDTH - MARGIN, MARGIN + row * CELL_SIZE), line_width)
        pygame.draw.line(screen, BLACK, (MARGIN + row * CELL_SIZE, MARGIN), 
                         (MARGIN + row * CELL_SIZE, HEIGHT - MARGIN), line_width)
    
    # Draw numbers
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            num = board[row][col]
            if num != 0:
                num_text = font.render(str(num), True, BLUE)
                text_rect = num_text.get_rect(center=(MARGIN + col * CELL_SIZE + CELL_SIZE // 2,
                                                      MARGIN + row * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(num_text, text_rect)
    
    # Highlight selected cell
    if selected_row is not None and selected_col is not None:
        pygame.draw.rect(screen, LIGHT_BLUE, 
                         (MARGIN + selected_col * CELL_SIZE, MARGIN + selected_row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 3)
 
    # Display message
    if message:
        message_text = message_font.render(message, True, RED if "Wrong" in message else GREEN)
        message_rect = message_text.get_rect(center=(WIDTH // 2, HEIGHT - 30))
        screen.blit(message_text, message_rect)
    
    # Display hint number if timer is active
    if hint_timer > 0:
        hint_text = message_font.render(f"Correct number: {hint_number}", True, RED)
        hint_rect = hint_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(hint_text, hint_rect)
 
    # Display winning message if the game is won
    if game_won:
        win_text = win_font.render("You have won the Game!", True, GREEN)
        win_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(win_text, win_rect)
 
def is_valid_move(row, col, num):
    """Check if the entered number matches the solution board."""
    return solution_board[row][col] == num
 
def check_win():
    """Check if the player's board matches the solution board."""
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] != solution_board[row][col]:
                return False
    return True
 
def handle_click(pos):
    global selected_row, selected_col
    x, y = pos
    if MARGIN <= x < WIDTH - MARGIN and MARGIN <= y < HEIGHT - MARGIN:
        selected_col = (x - MARGIN) // CELL_SIZE
        selected_row = (y - MARGIN) // CELL_SIZE
    else:
        selected_row, selected_col = None, None
 
def handle_keypress(key):
    global message, message_timer, hint_timer, hint_number, game_won
    if selected_row is not None and selected_col is not None:
        if key == pygame.K_BACKSPACE or key == pygame.K_DELETE:
            board[selected_row][selected_col] = 0
        elif pygame.K_1 <= key <= pygame.K_9:
            num = key - pygame.K_0
            if is_valid_move(selected_row, selected_col, num):
                board[selected_row][selected_col] = num
                if check_win():  # Check if the player has won
                    game_won = True  # Set game_won to True to display the winning message
                    message = "You Won!"
                else:
                    message = "Correct Entry!"
                message_timer = 200
            else:
                message = "Wrong Entry! Try again."
                message_timer = 200
                hint_number = solution_board[selected_row][selected_col]
                hint_timer = 100
 
def main():
    global message, message_timer, hint_timer
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_click(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                handle_keypress(event.key)
        
        if message_timer > 0:
            message_timer -= 1
        else:
            message = ""
        
        if hint_timer > 0:
            hint_timer -= 1
 
        draw_board()
        pygame.display.flip()
 
    pygame.quit()
 
if __name__ == "__main__":
    main()
 