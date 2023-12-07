# test_game.py

from jewel_columns import *
import unittest


class ColumnsGameTest(unittest.TestCase):
    def setUp(self):
        pass


    def initial_column_is_empty(self):
        OoColumnsGameTest = ColumnsGrid(4, 4)


        self.assertEqual(self._game_board.column(), 0)
    
    def test_after_moving_column_right(self):
        column = ColumnsGrid()
        self.assertEqual(self._game_board.column(), 1)

if __name__ == '__main__':
    unittest.main()
