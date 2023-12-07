'''
game_model.py
game mechanics
'''

class Jewel:
    def __init__(self, color: str):
        self._color = color

    @property
    def color(self):
        return self._color



class ColumnsGrid:
    def __init__(self, columns: int, rows: int):
        self._columns = columns
        self._rows = rows
        self._board = [[0 for j in range(self._columns)] for i in range (self._rows)]


    def initialize_empty_board_with_zeros(self, contents: list[str]) -> list[list:int]:
        board = []

        for i in range(self._columns):
            row = []
            for j in range(self._rows):
                row.append(0)
            board.append(row)
        
        print(board)
        return board

class ColumnsState:
    def board(self):
        '''board state'''
        self._Jewel.


    @staticmethod
    def get_board(self, columns, rows):
        return []
    
    def create_empty_board(self, columns, rows):
        for i in rows:
            for j in columns:
                self._board[i][j] = 0


    def column(self) -> int:
        return self._column
    
    def move_right(self):
        self._column += 1

    def move_left(self):
        self._column += 1

    def columns_logic(self):
        # if there are holes in the rows of the columns then
        # drop them down a row and repeat until no mo holes
        pass


class GameState:
    def __init__():
        pass

    
    def structure_the_faller(self, Jewel:[Jewel, Jewel, Jewel]) -> list:
        col = []
        for i in Jewel:
            row = []
            row.append(Jewel[i])
            col.append(row)
        return col    
        

    def handle_faller(self):
        pass