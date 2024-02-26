from tictactoe import *

# Test case 1: Player wins in a single game instance
def test_single_game_instance_win():
    game = MetaTicTacToe()
    # Manually set up a winning scenario in a single game instance
    game.game_boards[0] = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
    print("Before check_win_condition:")
    game.meta_box_id = 0
    game.print_board(game.game_boards[0])  # Print the game board before checking win condition
    assert game.check_win_condition() == True

# Test case 2: Player wins the meta-board horizontally
def test_meta_board_horizontal_win():
    game = MetaTicTacToe()
    # Manually set up a winning scenario in the meta-board horizontally
    game.meta_board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
    game.meta_box_id = -1
    assert game.check_meta_board_win_condition() == True

# Test case 3: Player wins the meta-board vertically
def test_meta_board_vertical_win():
    game = MetaTicTacToe()
    # Manually set up a winning scenario in the meta-board vertically
    game.meta_board = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
    assert game.check_meta_board_win_condition() == True

# Test case 4: Player wins the meta-board diagonally
def test_meta_board_diagonal_win():
    game = MetaTicTacToe()
    # Manually set up a winning scenario in the meta-board diagonally
    game.meta_board = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
    assert game.check_meta_board_win_condition() == True

# Test case 5: Meta Game ends in a tie
def test_game_tie():
    game = MetaTicTacToe()
    # Manually set up a tie scenario in a single game instance
    game.meta_board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
    assert game.check_meta_board_win_condition() == True


test_single_game_instance_win()
test_meta_board_horizontal_win()
test_meta_board_vertical_win()
test_meta_board_diagonal_win()
test_game_tie()

print("All test cases passed!")
