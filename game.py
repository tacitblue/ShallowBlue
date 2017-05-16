from board import Board
from display import Display
from player import Player
import os

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

    def play(self):
        while not self.board.over():
            self.play_turn()
            self.switch_turn()
        else:
            self.display.render()
            self.display.print_message("%s wins!   " % self.board.winner())
            self.display.textfield.refresh()
            self.display.sleep(2000)
            self.display.close()

    def play_turn(self):
        self.display.print_message("  %s's turn   " % self.current_player.color)

        move = self.current_player.get_move(self.board, self.display)
        from_pos = move[0]
        to_pos = move[1]

        self.board.move_piece(from_pos, to_pos)
        self.display.find(from_pos).refresh()
        self.display.find(to_pos).refresh()
        self.display.find(self.display.selection).refresh()
        self.display.selection = None

test = Game()
test.play()
