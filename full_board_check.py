import space_check
def full_board_check(board):
    for i in range(1,10):
        if space_check.space_check(board, i):
            return False
    return True
    pass