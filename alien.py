import pygame
import random


class Alien(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.attack = 0.3
        self.image = pygame.image.load('images/alienspaceship.png')
        self.image = pygame.transform.scale(self.image, (150, 130))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(20, 800)
        self.velocity = random.randint(1, 3)

    def remove(self):
        self.game.all_alien.remove(self)

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 830 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            #ajouter le nombre de points
            self.game.score += 1

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.y += self.velocity

        else:
            self.game.player.damage(10)
            self.remove()
            self.game.spawn_Alien()
        if self.rect.y > 550:
            self.remove()
            self.game.spawn_Alien()
