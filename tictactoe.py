import random
import sys

"""
This is a variation of the classic game of tic-tac-toe, where 2 players take turns
putting X's and O's in a 3x3 grid. In this version, there are 9 instances of the
game being played simultaneously. Each turn, a player may make a single move in
any one of the 9 game instances. The game instances are arranged in a 3x3 grid,
constituting a meta-game. A player wins the meta-game by getting 3 in a row
(horizontally, vertically, or diagonally) in the game instances. If a player wins
a game instance, they take the corresponding square in the meta-game. If a game
instance results in a tie, it is replaced with a fresh instance with no moves
played. The game is over when a player wins the meta-game.

Assumptions:
In this game, human has some privilage, they can decide which 
board the computer has to play if human wins the previous game
human by default can choose the next board if computer wins the 
game

The game ends when the a player wins meta board or both players are out of moves

I have added a 2nd human player, to test the game:

# meta_box_id -> board id
"""

class MetaTicTacToe:
    def __init__(self):
        self.meta_board = [[" " for _ in range(3)] for _ in range(3)]
        self.game_boards = [[[" " for _ in range(3)] for _ in range(3)] for _ in range(9)]
        self.current_player = "X"
        self.meta_board_dict = {0:[0,0],1:[0,1],2:[0,2],3:[1,0],4:[1,1],5:[1,2],
                           6:[2,0],7:[2,1],8:[2,2]}
        self.meta_box_id = -2
        self.id_row = -1
        self.id_col = -1
        self.win = ""
        self.finished_boards = [] # id's of boards that are done
        self.GameOver = False


    def print_all_boards(self):
        print("Meta-game:")
        for row in self.meta_board[:-1]:
            print(" | ".join(row))
            print("-" * 9)
        print(" | ".join(self.meta_board[-1]))

        print("Individual game instances:")
        print(" Board 0    Board 1   Board 2   Board 3   Board 4   Board 5   Board 6   Board 7   Board 8")
        for row in range(3):
            
            for meta_ele in range(9):
                #print(f"count:{meta_ele}")
                if meta_ele!=8:
                    print(" | ".join(self.game_boards[meta_ele][row]),end=" ")       
                else:
                    print(" | ".join(self.game_boards[meta_ele][row]))      
            if row == 2:
                print()
            else: print(("*"+"-" * 7+"* ")*9)

    def print_board(self,board):
        """
        Prints the current state of the given Tic-Tac-Toe board.
        Input: game board
        Return: None
        """
        if self.meta_box_id==-1:
            print("Meta Board")
        else:
            print("Board: ",self.meta_box_id)
        for row in board[:-1]:
            print(" | ".join(row))
            print("-" * 9)
        print(" | ".join(board[-1]))
        

    def find_empty_cells(self,board):
        """
        Finds all emplty cells in the board
        Input: game board
        Return: None
        """
        empty_cells = []
        for row_idx, row in enumerate(board):
            for col_idx, cell in enumerate(row):
                if cell == " ":
                    empty_cells.append((row_idx, col_idx))
        return empty_cells
    
    def check_meta_box_id_bounds(self):
        if self.meta_box_id>8 or self.meta_box_id<0:
                print("meta board id is out of bounds, last chance to give the correct value!")
                self.meta_box_id = int(input("Enter meta-box id (0-8): "))
                if self.meta_box_id>8 or self.meta_box_id<0:
                    print("meta board id is out of bounds")
                    sys.exit()
    
    def check_game_board(self, board):
        """
        Implements win and tie conditions for a single game instance
        Input: game board
        Return: True/-1/0
        1 -> if a player wins the game; -1 -> if there are moves still left; 0 -> if it is a tie
        """
        for row in board:
            if row[0] == row[1] == row[2] != " ":
                self.win = row[0]
                return 1
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != " ":
                self.win = board[0][col]
                return 1
        if board[0][0] == board[1][1] == board[2][2] != " ":
            self.win = board[0][0]
            return 1
        if board[0][2] == board[1][1] == board[2][0] != " ":
            self.win = board[0][2]
            return 1
        if all(all(cell != " " for cell in row) for row in board):
            print("It's a tie!")
            return 0
        return -1

    def check_board_row_col_bounds(self, number, name=''):
        """
        Checks the board's row/column bounds
        Input: row/col id and row/col
        Output: row/col id
        """
        if number>2 or number<0:
                print(f"{name} id in the board is out of bounds, last chance to give the correct value!")
                number = int(input(f"Enter {name} (0-2): "))
                if number>2 or number<0:
                    print(f"{name} id in the board is out of bounds")
                    sys.exit()
                return number
        return number

    def human_move(self):
        # Human player's move
        while True:
            # 0 is for meta board
            self.meta_box_id = -1
            #self.print_board(self.meta_board)
            self.print_all_boards()
            try:
                # 1 to 9 are the indices of the 3x3 meta board
                self.meta_box_id = int(input("Enter meta-box id (int value from 0 to 8): "))
                self.check_meta_box_id_bounds()
                if self.meta_board[self.meta_board_dict[self.meta_box_id][0]][self.meta_board_dict[self.meta_box_id][1]]!= " ":
                    print("That box is already taken. Try again.")
                    continue
                print("You selected the following board to play")
                self.print_board(self.game_boards[self.meta_box_id])
                self.id_row = int(input("Enter row (from 0 or 1 or 2): "))
                self.id_row = self.check_board_row_col_bounds(self.id_row,'row')
                self.id_col = int(input("Enter column (from 0 or 1 or 2): "))
                self.id_col = self.check_board_row_col_bounds(self.id_col,'col')
            except ValueError:
                print("\n--Invalid input, try again!--\n")
                continue

            if self.game_boards[self.meta_box_id][self.id_row][self.id_col] != " ":
                print("That position is already taken. Try again.")
                continue
            else:
                self.game_boards[self.meta_box_id][self.id_row][self.id_col] = self.current_player
                self.print_board(self.game_boards[self.meta_box_id])
                break
        
    def human_2_move(self):
        # This is used to replace computer player
        while True:
            self.id_row = int(input("Human 2, enter row (0-2): "))
            self.id_col = int(input("Human 2, enter column (0-2): "))
            if self.game_boards[self.meta_box_id][self.id_row][self.id_col] != " ":
                print("That position is already taken. Try again.")
                continue
            else:
                self.game_boards[self.meta_box_id][self.id_row][self.id_col] = self.current_player
                self.print_board(self.game_boards[self.meta_box_id])
                break

    def computer_move(self):
        # Random guessing computer player's move, from available moves
        empty_cells = self.find_empty_cells(self.game_boards[self.meta_box_id])
        row,col = random.choice(empty_cells)
        self.game_boards[self.meta_box_id][row][col] = self.current_player
        self.print_board(self.game_boards[self.meta_box_id])

    def check_meta_board_win_condition(self):
        #Check meta game board
        meta_board_result = self.check_game_board(self.meta_board)
        # When a player wins
        if meta_board_result==1:
            self.meta_box_id = -1
            self.print_board(self.meta_board)
            print(f"Player {self.win} wins the meta board!")
            self.GameOver = True
        # When it is a tie
        if meta_board_result==0:
            self.meta_box_id = -1
            self.print_board(self.meta_board)
            print(f"It is a tie in the meta board!")
            self.GameOver = True
        return self.GameOver

    def check_win_condition(self):
        """
        Checks if there is a win in the board.
        Return: True or False
        """
        result  = self.check_game_board(self.game_boards[self.meta_box_id])
        if result==1:
            r,c = self.meta_board_dict[self.meta_box_id]
            self.meta_board[r][c]=self.win
            self.finished_boards.append(self.meta_box_id)
            print(f"Player {self.win} wins the board {self.meta_box_id}!")
            self.check_meta_board_win_condition()
            if self.GameOver:
                return True
            self.win = ""
            return True
        #If there are moves still left in the game
        elif result==-1:
            pass
        #The game is tie, so reset the game (result == 0)
        else:
            self.game_boards[self.meta_box_id]=[[" " for _ in range(3)] for _ in range(3)]
        return False

    def main(self):
        # This function builds the 
        print("**** Initializing the game! ****")
        #self.print_all_boards()
        while True:
            print(f"Player {self.current_player}'s turn:")
            if self.current_player == "X":
                self.human_move()
            else:
                self.computer_move()
                #self.human_2_move()
            
            result = self.check_win_condition()
            if self.GameOver:
                print("Wonderful! The meta game is finished.")
                break
            # If human wins, make the human decide which board the next player plays
            if result and self.current_player=='X':
                self.meta_box_id = -1
                self.print_board(self.meta_board)
                count = 0
                while count<3:
                    self.meta_box_id = int(input("Enter meta-box id (0-8) for computer to play: "))
                    self.check_meta_box_id_bounds()
                    if self.meta_board[self.meta_board_dict[self.meta_box_id][0]][self.meta_board_dict[self.meta_box_id][1]]!= " ":
                        print(f"That box is already taken. Try again.\n Chances left {2-count}")
                        count = count+1
                        continue
                    else:break  
                if count==3:
                    print("You gave incorrect meta-box id 3 times")
                    sys.exit()
            self.current_player = "O" if self.current_player == "X" else "X"

if __name__ == "__main__":
    game = MetaTicTacToe()
    print("\n---------------- Welcome to the tic-tac-toe game! ----------------")
    print("\n---------------- You are player 'X' and computer is player 'O' ----------------")
    game.main()