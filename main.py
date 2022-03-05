import pygame
from pygame import *
from Perso import *

from map import *

if __name__ == '__main__':
    pygame.init()
    game = map()
    game.run()