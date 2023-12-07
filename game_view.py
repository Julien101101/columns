# the view tells the model what to do
import game_model


class ColumnsGame:
    # i am afraid to make a mistake but i will full send
    # how can i init something and use it with what ive 
    # made in the game model...
    def __init__(self, board: list[list[int]]):
        board = state

        

    def display_field(self):
        '''
        Prints the current board field
        '''
        for i in range(self.board):
            for j in range(self.board[i]):
                if self.board[i][j] == 0:
                    print(f"|", end = "")
                elif self.board[i][j] == -1:
                    print("|")
                # here i want to pass to use the board model and access the jewels
                else:
                    print(f" ", end = "")
                    print(self.board[i][j])
                    print(f" ", end = "")
        
        for i in range(len(self.board[i])):
            if i == 0:
                print(f" ", end = "")
            elif i == -1:
                print(f" ", end = "")
            else:
                print(f"---", end = "")

    
     
if __name__ == "__main__":
    initial_board = [[1, 2, 3, 4], [1, 2, 3, 4], [0, 0, 0, 0], [0, 0, 0, 1]]
    game_instance = ColumnsGame(4,4)
    game_instance.initialize_empty_board(initial_board)
    game_instance.display_field()