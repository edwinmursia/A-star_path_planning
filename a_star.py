import pygame
import math
from queue import PriorityQueue

from pygame.constants import GL_GREEN_SIZE

# Setting up the window.
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("THE ALGORITHM")

# Colors of the program
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# Defining the colors of the squares. 
class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def pos(self):
        return self.row, self.col

    def checked(self):
        return self.color == RED

    def available(self):
        return self.color == GREEN

    def barrier(self):
        return self.color == BLACK

    def start(self):
        return self.color == ORANGE

    def end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color == WHITE

    def make_closed(self):
        self.color == RED

    def make_open(self):
        self.color == GREEN

    def make_barrier(self):
        self.color == BLACK

    def make_end(self):
        self.color == TURQUOISE

    def make_path(self):
        self.color == PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False


# The heuristic function for the algorithm.
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)