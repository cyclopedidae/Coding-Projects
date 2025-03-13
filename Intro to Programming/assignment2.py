import random
from typing import List

def print_board(board: List[List[int]]) -> None:
    """
    This function receives a board and displays it with grid lines, such that 3x3 grids are
    separated by "-" horizontally and "|" vertically.

    >>> board =[[0,0,3,4,5,0,7,0,0],[4,0,0,8,2,9,1,0,0],[5,9,0,1,7,0,2,0,0],
    [2,0,0,3,0,5,8,0,7],[0,0,6,9,0,0,3,0,0],[3,8,9,0,0,0,5,6,0],
    [6,0,5,7,0,0,0,1,0],[8,0,2,6,0,1,4,3,5],[9,0,0,0,0,2,6,7,0]]
    >>> print_board(board)
        
    . . 3 | 4 5 . | 7 . . 
    4 . . | 8 2 9 | 1 . . 
    5 9 . | 1 7 . | 2 . . 
    ---------------------
    2 . . | 3 . 5 | 8 . 7 
    . . 6 | 9 . . | 3 . . 
    3 8 9 | . . . | 5 6 . 
    ---------------------
    6 . 5 | 7 . . | . 1 . 
    8 . 2 | 6 . 1 | 4 3 5 
    9 . . | . . 2 | 6 7 .
    """
    #TODO
        

# Check if a move is valid
def is_valid(board: List[List[int]], row: int, col: int, num: int) -> bool:
    #IN PROGRESS 
    """
    This function receives a board, row number (row), column number (col), and number (num) to be added and
    returns a boolean value indicating whether placing 'num' at (row, col) is valid.

    >>> board =[
    [0,0,3,4,5,0,7,0,0],
    [4,0,0,8,2,9,1,0,0],
    [5,9,0,1,7,0,2,0,0],
    [2,0,0,3,0,5,8,0,7],
    [0,0,6,9,0,0,3,0,0],
    [3,8,9,0,0,0,5,6,0],
    [6,0,5,7,0,0,0,1,0],
    [8,0,2,6,0,1,4,3,5],
    [9,0,0,0,0,2,6,7,0]]

    >>>is_valid(board,0,1,2)
    True
    >>>is_valid(board,0,0,2)
    False
    """
    # Check if num already in sublist
    # Check if num already in index of other sublists
    # Check if num already exists in sublist+1, same index and +1 and +2

# Check if board is completed
def is_complete(board: list[list[int]]) -> bool:
    #COMPLETE
    """
    This function receives a board and returns True if there are no empty cells.

    >>> board =[[0,0,3,4,5,0,7,0,0],[4,0,0,8,2,9,1,0,0],[5,9,0,1,7,0,2,0,0],
    [2,0,0,3,0,5,8,0,7],[0,0,6,9,0,0,3,0,0],[3,8,9,0,0,0,5,6,0],
    [6,0,5,7,0,0,0,1,0],[8,0,2,6,0,1,4,3,5],[9,0,0,0,0,2,6,7,0]]
    >>> is_complete(board)
    False

    >>> board = [[1,2,3,4,5,6,7,8,9],[4,6,7,8,2,9,1,5,3],[5,9,8,1,7,3,2,4,6],
    [2,1,4,3,6,5,8,9,7],[7,5,6,9,1,8,3,2,4],[3,8,9,2,4,7,5,6,1],
    [6,3,5,7,8,4,9,1,2],[8,7,2,6,9,1,4,3,5],[9,4,1,5,3,2,6,7,8]]
    >>> is_complete(board)
    True
    """
    for sublist in board:
        for number in sublist:
            if number == 0:
                return False
            else: return True

# Find all empty cells
def find_empty_cells(board: List[List[int]]) -> List[List[int]]:
    """
    This function receives a board and returns a list of [row, col] positions where the
    cells are empty (. or [0]).

    >>> board =[[0,0,3,4,5,0,7,0,0],[4,0,0,8,2,9,1,0,0],[5,9,0,1,7,0,2,0,0],
    [2,0,0,3,0,5,8,0,7],[0,0,6,9,0,0,3,0,0],[3,8,9,0,0,0,5,6,0],
    [6,0,5,7,0,0,0,1,0],[8,0,2,6,0,1,4,3,5],[9,0,0,0,0,2,6,7,0]]
    >>> empty = find_empty_cells(board)
    >>> empty
    [[0, 0], [0, 1], [0, 5], [0, 7], [0, 8], [1, 1], [1, 2], [1, 7], [1, 8],
    [2, 2], [2, 5], [2, 7], [2, 8], [3, 1], [3, 2], [3, 4], [3, 7], [4, 0],
    [4, 1], [4, 4], [4, 5], [4, 7], [4, 8], [5, 3], [5, 4], [5, 5], [5, 8],
    [6, 1], [6, 4], [6, 5], [6, 6], [6, 8], [7, 1], [7, 4], [8, 1], [8, 2],
    [8, 3], [8, 4], [8, 8]]
    """
    #TODO
    


# Give a hint by placing a correct number in an empty cell
def give_hint(board: List[List[int]], solved_board: List[List[int]]) -> None:
    """
    This function receives the a board and the answer (solved_board),
    finds an empty cell, fills it with the correct number, and
    prints a message indicating what it did. If the board was already complete,
    it prints a message indicating that there are no hints left.

    >>> board =[[0,0,3,4,5,0,7,0,0],[4,0,0,8,2,9,1,0,0],[5,9,0,1,7,0,2,0,0],
    [2,0,0,3,0,5,8,0,7],[0,0,6,9,0,0,3,0,0],[3,8,9,0,0,0,5,6,0],
    [6,0,5,7,0,0,0,1,0],[8,0,2,6,0,1,4,3,5],[9,0,0,0,0,2,6,7,0]]
    
    >>> solved_board = [[1,2,3,4,5,6,7,8,9],[4,6,7,8,2,9,1,5,3],[5,9,8,1,7,3,2,4,6],
    [2,1,4,3,6,5,8,9,7],[7,5,6,9,1,8,3,2,4],[3,8,9,2,4,7,5,6,1],
    [6,3,5,7,8,4,9,1,2],[8,7,2,6,9,1,4,3,5],[9,4,1,5,3,2,6,7,8]]

    >>> give_hint(board,solved_board)
    Hint: Placed 1 at (0, 0)

    >>> board = [[1,2,3,4,5,6,7,8,9],[4,6,7,8,2,9,1,5,3],[5,9,8,1,7,3,2,4,6],
    [2,1,4,3,6,5,8,9,7],[7,5,6,9,1,8,3,2,4],[3,8,9,2,4,7,5,6,1],
    [6,3,5,7,8,4,9,1,2],[8,7,2,6,9,1,4,3,5],[9,4,1,5,3,2,6,7,8]]
    
    >>> solved_board = [[1,2,3,4,5,6,7,8,9],[4,6,7,8,2,9,1,5,3],[5,9,8,1,7,3,2,4,6],
    [2,1,4,3,6,5,8,9,7],[7,5,6,9,1,8,3,2,4],[3,8,9,2,4,7,5,6,1],
    [6,3,5,7,8,4,9,1,2],[8,7,2,6,9,1,4,3,5],[9,4,1,5,3,2,6,7,8]]

    >>> give_hint(board, solved_board)
    No hints available! The board is already complete.
    """

    #TODO

"""
You do not need to understand the code below, it is there to allow the game to run.
If you are curious, try to go through the code and the comments to figure out how it works.

Please note that this is not the best way to write this code. It is written this way to
allow you to understand it in case you choose to, and therefore avoids more advanced approaches.

"""
# Play Sudoku
def play_sudoku() -> None:
    """This function runs the sudoku game loop."""
    board, solved_board = generate_random_board()  # Get puzzle & solution
    
    while not is_complete(board):
        print("\nYour current board:")
        print_board(board)
        print("\nOptions: Enter row (0-8), col (0-8), num (1-9) OR 'quit' OR 'hint'.")
        
        user_input = input("Enter your move: ").strip().lower()

        if user_input == "quit":
            print("\nYour current board:")
            print_board(board)
            print("\nThe correct completed board:")
            print_board(solved_board)  # Show the full solved board
            print("\nThanks for playing! Goodbye. 👋")
            break

        if user_input == "hint":
            give_hint(board, solved_board)
            continue
        
        parts = user_input.split()
        if len(parts) != 3 or not all(part.isdigit() for part in parts):
            print("Invalid input! Format: row col num (e.g., '2 3 5').")
            continue

        row, col, num = map(int, parts)
        if not (0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9):
            print("Invalid numbers! Row/Col must be 0-8, Num must be 1-9.")
            continue

        if board[row][col] != 0:
            print("Invalid move! Cell already filled.")
            continue
        
        if is_valid(board, row, col, num):
            board[row][col] = num
        else:
            print("Invalid move! Number already exists in row, column, or 3x3 grid.")

    if is_complete(board):
        print("\n🎉 Congratulations! You solved the Sudoku! 🎉")
        print_board(board)

# Generate a board with some numbers removed
def generate_random_board() -> List[List[int]]:
    """Generates a playable Sudoku board with randomized numbers and locations."""
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)  # Fill board randomly with a valid solution
    solved_board = [row[:] for row in board]  # Save completed solution

    # Remove numbers to create a puzzle
    attempts = 40  # More removals = harder puzzle
    while attempts > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
        attempts -= 1

    return board, solved_board


        
# Solve Sudoku using backtracking (used for board generation)
def solve_sudoku(board: List[List[int]]) -> bool:
    """Solves the Sudoku puzzle using backtracking."""
    empty_cells = find_empty_cells(board)
    if not empty_cells:
        return True  # Board is solved

    row, col = empty_cells[0]  # Get the first empty cell

    for num in random.sample(range(1, 10), 9):  # Randomize number placement
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):  # Move to the next empty cell
                return True
            board[row][col] = 0  # Reset on failure

    return False

# Start the game
if __name__ == "__main__":
    play_sudoku()
