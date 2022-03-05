
import pygame
from pygame import *
from Perso import *
from time import *

class map:
    def __init__(self):
        self.fenetre = pygame.display.set_mode((1024, 800))
        pygame.display.set_caption("JEU - Projet3")

        self.player = Perso(512, 400)

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.haut()
        elif pressed[pygame.K_DOWN]:
            self.player.bas()
        elif pressed[pygame.K_RIGHT]:
            self.player.droite()
        elif pressed[pygame.K_LEFT]:
            self.player.gauche()
        else:
            self.player.image = self.player.get_image("Image\sur_place.png")

    def run(self):
        jeu_en_cour = True

        clock = pygame.time.Clock()

        while jeu_en_cour:
            self.handle_input()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jeu_en_cour = False
            self.fenetre.fill((0, 0, 0))
            self.fenetre.blit(self.player.image, self.player.position)
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
