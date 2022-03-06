import pygame
import pygame_menu
import Game


class Obstacle:
    def __init__(self, x, y):
        self.image = pygame.image.load("Image/Decors/obstacle.png")
        self.rect = self.image.get_rect()
        self.position = [x, y]

    def get_image(self, image):
        assert type(image) == str, "La direction du fichier n'est pas un string"
        self.image = pygame.image.load(image)

    def update(self):
        self.rect.topleft = self.position



