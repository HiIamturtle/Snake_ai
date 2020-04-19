# Libraries
import config
from food import Food
from p5 import *
import numpy as np


class Snake:
    def __init__(self, board=None, show_board=None):
        self.board = board
        self.show_board = show_board
        self.cells = []
        self.length = 2
        self.food_pos = None

    def show(self):
        if self.board == 1:
            rect(())


