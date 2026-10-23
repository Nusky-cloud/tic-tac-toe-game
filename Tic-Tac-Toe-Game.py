# please note that the character 'x' represents first player's token
# please note that the character 'o' represents second player's token
import numpy

def draw_game_board():
    no_of_columns = int(input("How many columns? "))
    no_of_rows = int(input("How many rows? "))
    for row in range(no_of_rows + 1):
        print()
        for column in range(no_of_columns):
            print(" ", "-" * 3, end="")
        print()
        if row != no_of_rows:
            for column2 in range(no_of_columns + 1):
                print("|", " " * 3, end="")

def check_winner_in_the_list(game_board_values, empty_token):
    # using set to eliminate duplicates in the list and if the result set has only one element and the element is not equal to empty token, then the player has won
    row_as_set = ()
    for row_index in range(len(game_board_values)):
        row_as_set = set(game_board_values[row_index])
        if len(row_as_set) == 1 and game_board_values[row_index][0] != empty_token:
            if game_board_values[row_index][0] == 'x':
                return 1
            elif game_board_values[row_index][0] == 'o':
                return 2
    return 0

def check_winner_diagonally(game_board_values, empty_token):
    if game_board_values[1][1] != empty_token: # ignoring checking for winner diagonally if the game board center value is equal to empty token
        diagonal1 = set([game_board_values[0][0], game_board_values[1][1], game_board_values[2][2]])
        diagonal2 = set([game_board_values[0][2], game_board_values[1][1], game_board_values[2][0]])
        if len(diagonal1) == 1 or len(diagonal2) == 1:
            if game_board_values[1][1] == 'x':
                return 1
            elif game_board_values[1][1] == 'o':
                return 2
    return 0

def start_to_check_the_winner(matrix, empty_token):
    winner = 0
    winner = check_winner_in_the_list(matrix, empty_token) # check the winner horizontally in the matrix
    if winner == 0:
        winner = check_winner_in_the_list(numpy.transpose(matrix), empty_token) # check the winner vertically in the matrix
        if winner == 0:
            winner = check_winner_diagonally(matrix, empty_token)
            if winner == 0:
                print("Sorry! Nobody won")
            else:
              print(f"Winner is player {winner}")  
        else:
           print(f"Winner is player {winner}")     
    else:
        print(f"Winner is player {winner}")

    return winner

def play_tic_tac_toe_with_predefined_values():
    winner_is_2 = [['o', 'o', '.'],
                    ['o', 'x','.'],
                    ['o', 'x', 'o']]

    winner_is_1 = [['x', 'o', '.'],
                    ['o','x','.'],
                    ['o', 'x', 'x']]

    winner_is_also_1 = [['.', 'x', '.'],
                        ['o', 'x', '.'],
                        ['o', 'x', 'x']]

    no_winner = [['x', 'o', '.'],
                ['o', 'x', '.'],
                ['o', 'x', 'o']]

    also_no_winner = [['x', 'o', '.'],
                    ['o', 'x', '.'],
                    ['o', 'x', '.']]
    
    start_to_check_the_winner(winner_is_2, 0)
    start_to_check_the_winner(winner_is_1, 0)
    start_to_check_the_winner(winner_is_also_1, 0)
    start_to_check_the_winner(no_winner, 0)
    start_to_check_the_winner(also_no_winner, 0)

def place_the_token(game_board, player, no_of_positions_filled):
    player_input = input(f"Dear Player {player}, Please specify the position as row, col : ")
    player_row_position = int(player_input.split(",")[0]) - 1
    player_column_position = int(player_input.split(",")[1]) - 1

    if (0 <= player_row_position <= 2) and (0 <= player_column_position <= 2):
        if game_board[player_row_position][player_column_position] in ('x', 'o'):
            print("Wrong place! already token placed")
        else:
            if player == 1:
                game_board[player_row_position][player_column_position] = 'x'
            else:
                game_board[player_row_position][player_column_position] = 'o'

            no_of_positions_filled[0] += 1
                
            for row in range(len(game_board)):
                print(game_board[row])
    else:
        print("input should between 1 or 2 or 3")

def play_tic_tac_toe_with_user_input():
    game_board = [(['.'] * 3) for i in range(3)]
    no_of_positions_filled = [0]

    while no_of_positions_filled[0] < 9:
        place_the_token(game_board, 1, no_of_positions_filled)
        if no_of_positions_filled[0] == 9:
            break
        place_the_token(game_board, 2, no_of_positions_filled)
    
    return start_to_check_the_winner(game_board, '.')

def play_multiple_times():
    winner = 0
    player1_winning_times = 0
    player2_winning_times = 0
    play_again = 'y'

    while play_again == 'y':
        winner = play_tic_tac_toe_with_user_input()
        if winner == 1:
            player1_winning_times += 1
        elif winner == 2:
            player2_winning_times += 1
        play_again = input("Do you want to play again (y/n) ? ")

    print("Game Over!")
    print(f"No of times Player 1 won : {player1_winning_times}")
    print(f"No of times Player 2 won : {player2_winning_times}")
    if player1_winning_times > player2_winning_times:
        print("Winner is Player 1")
    elif player1_winning_times < player2_winning_times:
        print("Winner is Player 2")

if __name__ == "__main__":
    # step 1
    #draw_game_board()

    # step 2
    #play_tic_tac_toe_with_predefined_values()

    # step 3
    # play_tic_tac_toe_with_user_input()

    # step 4
    play_multiple_times()