import pygame

from game import Game

# generer la fenetre de notre jeu
pygame.display.set_caption("game")
screen = pygame.display.set_mode((900, 620))

# importer et charger l'arr plan de notre jeu
backGround = pygame.image.load('images/background.jpg').convert()
y = 0

#importer charger notre bannière
banner = pygame.image.load('images/spaceshooter.jpeg')
banner = pygame.transform.scale(banner, (900, 620))
banner_rect = banner.get_rect()
#banner_rect.x = screen.get_width() / 4

#import charger notre boutton pour lancer la partie
play_button = pygame.image.load('assets/assets/button.png')
play_button = pygame.transform.scale(play_button, (300, 100))
play_button_rect = play_button.get_rect()
play_button_rect.x = play_button.get_width() / 1.02
play_button_rect.y = play_button.get_height() / 0.29

# charger notre jeu
game = Game()

pygame.init()
CLOCK = pygame.time.Clock()
FPS = 200


running = True

# boucle tant que cette condition est vrai
while running:
    rel_y = y % backGround.get_rect().height

    # appliquer l'arr plan de notre jeu
    screen.blit(backGround, (0, rel_y - backGround.get_rect().height))
    if rel_y < 620:
        screen.blit(backGround, (0, rel_y))
    y += 1
    pygame.draw.line(screen, (0, 0, 0), (0, rel_y), (900, rel_y), 3)
    CLOCK.tick(FPS)
    #verifier si notre jeu a commencé ou non
    if game.is_playing:
        game.update(screen)
    else:
        #ajouter mon ecran de bienvenue
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)
    # mettre a jour la fenetre
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # verifier que l'even est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        #detecter su un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
                game.sound_manager.play('click')
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                #metter le jeu en mode lancer
                game.start()


