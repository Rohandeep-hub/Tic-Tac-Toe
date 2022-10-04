import space_check
def player_choice(board):
    position=0
    while position not in range(1,10) or not space_check.space_check(board,position):
        position = int(input('Choose your next position: (1-9) '))
    return position
    pass