# Libraries
import config
from p5 import *
import numpy as np


def setup():
    size(config.width, config.height)
    config.board = np.zeros((config.rows, config.columns))


def draw():
    background(51)


if __name__ == '__main__':
    run()
