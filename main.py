import player_input
import choose_first
import display_board
import replay   
import full_board_check
import place_marker
import player_choice
import space_check
import win_check
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input.player_input()
    turn = choose_first.choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter y or n.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board.display_board(theBoard)
            position = player_choice.player_choice(theBoard)
            place_marker.place_marker(theBoard, player1_marker, position)

            if win_check.win_check(theBoard, player1_marker):
                display_board.display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check.full_board_check(theBoard):
                    display_board.display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board.display_board(theBoard)
            position = player_choice.player_choice(theBoard)
            place_marker.place_marker(theBoard, player2_marker, position)

            if win_check.win_check(theBoard, player2_marker):
                display_board.display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check.full_board_check(theBoard):
                    display_board.display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay.replay():
        break