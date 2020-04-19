# Libraries
import config
from snake import Snake
from food import Food
from p5 import *
import numpy as np


class Game:
    def __init__(self, show=False):
        self.show = show
        self.win_width = config.width
        self.win_height = config.height

        self.rows = config.rows
        self.cols = config.columns

        self.cell_w = self.win_width / self.cols
        self.cell_h = self.win_height / self.rows

        self.board = np.zeros((self.rows, self.cols))
        self.show_board_rows = np.zeros((self.cols, 1))
        self.show_board_cols = np.zeros((self.cols, 1))
        self.gen_board()

        self.snake = Snake(board=self.board)

    def gen_board(self):
        if self.show:
            for row, i in enumerate(self.show_board_rows):
                i[0] = row * self.cell_h

            for col, i in enumerate(self.show_board_cols):
                i[0] = col * self.cell_w

    def test(self):
        if self.show:
            for i in self.show_board_rows:
                for j in self.show_board_cols:
                    print((i[0], j[0]))
                    rect((i[0], j[0]), self.cell_w / 1.25, self.cell_h / 1.25)


game = Game(show=True)


def setup():
    size(config.width, config.height)


def draw():
    background(51)
    game.test()


if __name__ == '__main__':
    run()
