import pygame
import random
from player import Player
from alien import Alien
from meteor import Meteor
from sounds import soundManager
pygame.init()

class Game:
    def __init__(self):
        # definir si notre jeu a commencé ou non
        self.is_playing = False
        # generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # groupe d'alien
        self.all_alien = pygame.sprite.Group()
        # groupe de meteor
        self.all_meteor = pygame.sprite.Group()
        # gerer le son
        self.sound_manager = soundManager()
        self.pressed = {}
        self.spawn_Alien()
        self.spawn_Alien()
        self.spawn_meteor()
        self.spawn_meteor()
        #mettre le score à 0
        self.score = 0

    def start(self):
        self.is_playing = True

    def sound_explosion(self):
        self.sound_manager.play('explosion')

    def score_sound(self):
        self.sound_manager.play('score')

    def game_over(self):
        # remettre le jeu à neuf, retirer les monstres, remettre le joueur a 100% de vie
        self.all_players = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0

    def update(self, screen):
        #afficher le score sur l'ecran
        font = pygame.font.SysFont("monospace", 16)
        score_text = font.render(f"Score : {self.score} ", 1, (255, 255, 255))
        screen.blit(score_text, (20, 20))
        # appliquer l'image de notre joueur
        screen.blit(self.player.image, self.player.rect)

        # recuperer les pro du joueur
        for projectile in self.player.all_projectiles:
            projectile.move_up()

        # recuperer les aliens de  notre joueur
        for alien in self.all_alien:
            alien.forward()

        # recuperer les meteors de notre jeu
        for meteor in self.all_meteor:
            meteor.forward()

        # appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        self.player.update_health_bar(screen)


        # appliquer l'ensemble des images d'alien
        self.all_alien.draw(screen)
        # appliquer l'ensemble des images de grp meteor
        self.all_meteor.draw(screen)

        # verifier si le joueur souhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 815:
            self.player.move_right()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 10:
            self.player.move_left()

        elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 10:
            self.player.move_up()

        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y < 540:
            self.player.move_down()

        print(self.player.rect.y)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_Alien(self):
        alien = Alien(self)
        self.all_alien.add(alien)

    def spawn_meteor(self):
        meteor = Meteor(self)
        self.all_meteor.add(meteor)