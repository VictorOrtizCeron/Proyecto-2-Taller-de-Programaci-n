import pygame
import random
import os
from os import path



WIDTH = 600
HEIGHT = 800
FPS = 60
isJump = False
jumpCount = 10

#definicion de colores utiles
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

game_folder = os.path.dirname(__file__)
ass_folder = os.path.join(game_folder, 'ProyAssets')




#initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Le potato")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
#busca la fuente mas similar a la especificada en el sistema
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    #El true aplica anti-aliasing al texto
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(Nav_img,(50,38))
        #transform.scale lo que hace es que cambia el tamano de la imagen
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        #esto cambia la caja de colision del jugador por un circulo
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        #este comando dibuja un circulo en el centro del jugador para asi poder entender que tamano usar
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 10
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -8
        if keystate[pygame.K_d]:
            self.speedx = 8
        if keystate[pygame.K_w]:
            self.speedy = -8
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0



        
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
      
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(Img_Rocas)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85  / 2)
        #Aca este radio me da el ancho del rectangulo de colision entre 2
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center



    def update(self):
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Rayo_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

#graficos del juego
background = pygame.image.load(path.join(ass_folder, 'GameBG.png')).convert()
background_rect = background.get_rect()
Nav_img= pygame.image.load(path.join(ass_folder, 'Tanque.png')).convert()
Rayo_img= pygame.image.load(path.join(ass_folder, 'Rayo.png')).convert()
Img_Rocas = []
List_Rocas = ['Roca.png','RocaG1.png', 'RocaG2.png', 'RocaS.png', 'RocaXS.png']
for img in List_Rocas:
    Img_Rocas.append(pygame.image.load(path.join(ass_folder, img)).convert())


all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

score = 0
lives = 3
#Game loop
running = True
while running:
    clock.tick(FPS)
    #Process input (events)
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

            


    #Update
    all_sprites.update()
    #revisar si las balas pegan
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 50 - hit.radius
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

    #revisar si hay colision
    hits=pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    #El collide_circle, especifica que usara el circulo de colision en vez de un rectangulo
    #el parentesis funciona asi: El sprite que se va a revisar, el grupo de sprites a revisar, 
    #si se quiere que se elimine el sprite que colisiono
    if hits:
        lives -= 1
    
    if lives == 0:
        running = False

    #Draw / render
    #Draw / render
    screen.fill((BLACK))
    screen.blit(background, background_rect)
    #blit, es un termino que hace referencia a una imagen, en este caso la imagen de fondo
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH / 2, 10)
    draw_text(screen, str(lives), 18, WIDTH-100, 10)
    #mostrar texto, el texto, el score, el ancho del texto, el alto del texto
    # los colores funcionan con RGB, no con hexadecimales, todos los colores = blanco
    # ningun color = negro, los valores van de 0 a 255
    # al final siempre hacer flip
    pygame.display.flip()

pygame.quit()
pass


