import threading
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TicTacToeException(Exception):
    """Custom exception class for Tic Tac Toe game."""
    pass


class TicTacToe:
    """A class to represent a Tic Tac Toe game."""

    def __init__(self):
        self.lock = threading.Lock()
        self.board = [' '] * 9
        self.current_player = 'X'
        self.game_over = False
        logging.info("Initialized new Tic Tac Toe game.")

    def display_board(self):
        """Display the current state of the board."""
        board = self.board
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("--+---+--")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("--+---+--")
        print(f"{board[6]} | {board[7]} | {board[8]}")
        logging.info("Displayed the board.")

    def make_move(self, position):
        """Make a move on the board."""
        with self.lock:
            if self.game_over:
                raise TicTacToeException("Game is already over.")
            if self.board[position] != ' ':
                raise TicTacToeException("Position already taken.")
            self.board[position] = self.current_player
            logging.info(f"Player {self.current_player} made a move at position {position}.")
            if self.check_winner():
                self.game_over = True
                logging.info(f"Player {self.current_player} wins!")
                print(f"Player {self.current_player} wins!")
            elif ' ' not in self.board:
                self.game_over = True
                logging.info("The game is a draw.")
                print("The game is a draw.")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                logging.info(f"Switched player to {self.current_player}.")

    def check_winner(self):
        """Check if the current player has won."""
        b = self.board
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)  # diagonals
        ]
        for x, y, z in win_conditions:
            if b[x] == b[y] == b[z] != ' ':
                return True
        return False

    def reset_game(self):
        """Reset the game to start a new one."""
        with self.lock:
            self.board = [' '] * 9
            self.current_player = 'X'
            self.game_over = False
            logging.info("Game has been reset.")

    def pause_game(self):
        """Pause the game."""
        logging.info("Game paused. Press any key to continue.")
        input("Game paused. Press any key to continue...")

    def quit_game(self):
        """Quit the game."""
        logging.info("Game quit by user.")
        print("Game quit. Goodbye!")
        exit()


def main():
    """Main function to run the Tic Tac Toe game."""
    game = TicTacToe()
    while True:
        game.display_board()
        command = input(f"Player {game.current_player}, enter your move (0-8) or command (p: pause, n: new, q: quit): ")
        if command == 'p':
            game.pause_game()
        elif command == 'n':
            game.reset_game()
        elif command == 'q':
            game.quit_game()
        else:
            try:
                position = int(command)
                if position < 0 or position > 8:
                    raise ValueError("Invalid position.")
                game.make_move(position)
            except (ValueError, TicTacToeException) as e:
                logging.error(e)
                print(e)


if __name__ == "__main__":
    main()
