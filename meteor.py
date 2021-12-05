import pygame
import random




class Meteor(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.attack = 0.3
        # definir l'image
        self.image = pygame.image.load('images/meteor1.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(20, 800)


    def remove(self):
        self.game.all_meteor.remove(self)

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
            self.game.spawn_meteor()
        if self.rect.y > 550:
            self.remove()
            self.game.spawn_meteor()
