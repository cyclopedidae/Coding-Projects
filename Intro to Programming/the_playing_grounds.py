board =[[1,2,3,4,5,6,7,8,9],[4,6,7,8,2,9,1,5,3],[5,9,8,1,7,3,2,4,6],
    [2,1,4,3,6,5,8,9,7],[7,5,6,9,1,8,3,2,4],[3,8,9,2,4,7,5,6,1],
    [6,3,5,7,8,4,9,1,2],[8,7,2,6,9,1,4,3,5],[9,4,1,5,3,2,6,7,8]]

def is_complete(board: list[list[int]]) -> bool:
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
    #IN PROGRESS

    for sublist in board:
        for number in sublist:
            if number == 0:
                return False
            else: return True

print(is_complete(board))