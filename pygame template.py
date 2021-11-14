import pygame
import random

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

#initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mrrp")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()

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
    screen.fill((BLACK))
    all_sprites.draw(screen)
    # los colores funcionan con RGB, no con hexadecimales, todos los colores = blanco
    # ningun color = negro, los valores van de 0 a 255
    # *after* everything, flip the display
    pygame.display.flip()

pygame.quit()


