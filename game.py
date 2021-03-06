from board import Board
from display import Display, sleep
from player import Player
from ai_player import AIPlayer


class Game(object):
    def __init__(self):
        self.board = Board()
        self.player1 = Player("white")
        self.player2 = Player("black")
        self.display = Display(self.board)
        self.current_player = self.player1

    def switch_turn(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1
        self.board.clear_pawn_vulnerabilities(self.current_player.color)

    def end_game(self):
        self.display.render()
        self.display.print_message("%s wins!   " % self.board.winner())
        self.display.textfield.refresh()
        sleep(2000)
        self.display.close()

    def play(self):
        while not (self.board.over() or self.display.terminate):
            self.play_turn()
            self.switch_turn()
        else:
            if self.board.over():
                self.end_game()
            else:
                self.display.close()

    def play_turn(self):
        self.display.print_message("  %s's turn   " % self.current_player.color)
        self.display.textfield.refresh()

        move = self.current_player.get_move(self.board, self.display)

        if not self.display.terminate:
            from_pos = move[0]
            to_pos = move[1]

            self.board.move_piece(from_pos, to_pos)

            if not isinstance(self.current_player, AIPlayer):
                self.display.selection = None
            self.display.render()


test = Game()
test.play()
