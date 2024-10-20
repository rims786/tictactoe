
import unittest
from tictactoe.tic_tac_toe import TicTacToe, TicTacToeException
class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def test_initial_state(self):
        self.assertEqual(self.game.board, [' '] * 9)
        self.assertEqual(self.game.current_player, 'X')
        self.assertFalse(self.game.game_over)

    def test_make_move(self):
        self.game.make_move(0)
        self.assertEqual(self.game.board[0], 'X')
        self.assertEqual(self.game.current_player, 'O')

    def test_invalid_move(self):
        self.game.make_move(0)
        with self.assertRaises(TicTacToeException):
            self.game.make_move(0)

    def test_winner(self):
        self.game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(self.game.check_winner())

    def test_draw(self):
        self.game.board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        self.game.make_move(8)
        self.assertTrue(self.game.game_over)

if __name__ == '__main__':
    unittest.main()
