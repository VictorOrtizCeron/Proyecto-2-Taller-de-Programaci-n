import pygame
import random
import os

from pygame.constants import BLEND_MULT

WIDTH = 800
HEIGHT = 600
FPS = 30

#definicion de colores utiles
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_folder = os.path.dirname(__file__)
ass_folder = os.path.join(game_folder, 'ProyAssets')


class Player(pygame.sprite.Sprite):
    #sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(ass_folder, 'p1_jump.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 5
    
    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


#initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mrrp")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#Game loop
running = True
while running:
    clock.tick(FPS)
    #Process input (events)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False

    #Update
    all_sprites.update()

    #Draw / render
    screen.fill((BLUE))
    all_sprites.draw(screen)
    # los colores funcionan con RGB, no con hexadecimales, todos los colores = blanco
    # ningun color = negro, los valores van de 0 a 255
    # *after* everything, flip the display
    pygame.display.flip()

pygame.quit()


