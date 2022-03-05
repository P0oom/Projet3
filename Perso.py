import pygame.image


class Perso(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = self.get_image("Image\sur_place.png")
        self.rect = self.image.get_rect()
        self.position = [x, y]

    def update(self):
        self.rect.topleft = self.position


    def get_image(self, nom_du_fichier):
        image = pygame.image.load(nom_du_fichier)
        return image

    def droite(self):
        self.position[0] += 10
        self.image = self.get_image("Image\droite.png")
    def gauche(self):
        self.position[0] -= 10
        self.image = self.get_image("Image\gauche.png")

    def haut(self):
        self.position[1] -= 10
        self.image = self.get_image("Image\saut.png")

    def bas(self):
        self.position[1] += 10
        self.image = self.get_image("Image\chute.png")
