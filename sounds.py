import pygame

class soundManager:

    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound("sounds/click.wav"),
            'explosion': pygame.mixer.Sound("sounds/explosion.wav"),
            'score': pygame.mixer.Sound("sounds/score.wav")
        }

    def play(self, name):
        self.sounds[name].play()