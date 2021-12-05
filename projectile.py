import pygame

# definir la classe qui va gérer le projectile de notre joueur
class Projectille(pygame.sprite.Sprite):
    #definir le cons de cette classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('images/rocket.png')
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 25
        self.rect.y = player.rect.y + 50
        self.origin_image = self.image
        self.angle = 0



    def remove(self):
        self.player.all_projectiles.remove(self)

    def move_up(self):
        self.rect.y -= self.velocity
        # self.rotate()

        # verifier si le projectille entre en collision avec un monster
        for alien in self.player.game.check_collision(self, self.player.game.all_alien):
            self.remove()
            alien.remove()
            self.player.game.spawn_Alien()
            self.player.game.score += 1
            self.player.game.sound_explosion()

        for meteor in self.player.game.check_collision(self, self.player.game.all_meteor):
            self.remove()
            meteor.remove()
            self.player.game.spawn_meteor()
            self.player.game.score += 1

        if self.rect.y < 0:
            self.remove()
