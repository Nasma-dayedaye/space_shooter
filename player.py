import pygame
import random


pygame.init()
from projectile import Projectille


# creer une premiere classe qui va controller notre joueur
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('images/spaceship.png')
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.x = 420
        self.rect.y = 540

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si le joueur n'a plus de points de vie
            self.game.game_over()

    def launch_projectile(self):
        self.all_projectiles.add(Projectille(self))

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_alien):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        if not self.game.check_collision(self, self.game.all_alien):
            self.rect.y -= self.velocity

    def move_down(self):
        if not self.game.check_collision(self, self.game.all_alien):
            self.rect.y += self.velocity

    def update_health_bar(self, surface):
        # definir une couleur pour notre jauge de vie (vert claire)
        bar_color = (255, 0, 0)
        # definir une autre couleur pour le back de la jauge (gris foncé)
        back_bar_color = (60, 60, 60)

        # definir la position de notre jauge de vie ainsi que sa largeur et son epaisseur
        bar_position = [self.rect.x - 13, self.rect.y + 70, self.health, 5]

        back_bar_position = [self.rect.x - 13, self.rect.y + 70, self.max_health, 5]
        # dessiner notre barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
