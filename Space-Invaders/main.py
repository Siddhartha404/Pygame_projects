import pygame
import pygame.display
from random import randint


#initializing
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")
running = True
clock = pygame.time.Clock()


#saceship
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, groups, img):
        super().__init__(groups)
        self.image = img
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT-50))
        self.direction = pygame.math.Vector2(1,1)
        self.speed = 300
    def update(self, dt):
        #spaceship movement
        key = pygame.key.get_pressed()
        self.direction.x = int(key[pygame.K_RIGHT]) - int(key[pygame.K_LEFT])
        self.direction.y = int(key[pygame.K_DOWN]) - int(key[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, img):
        super().__init__(groups)   
        self.image = img
        self.rect = self.image.get_frect(center=((randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT))))
    
class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups, img):
        super().__init__(groups)   
        self.image = img
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, img):
        super().__init__(groups)   
        self.image = img
        self.rect = self.image.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))

#all imports
spaceship_img = pygame.image.load('images/spaceship.png').convert_alpha()
star_img = pygame.image.load('images/star.png').convert_alpha()
metero_img = pygame.image.load('images/meteor.png').convert_alpha()
laser_img = pygame.image.load('images/laser.png').convert_alpha()

all_sprite = pygame.sprite.Group()
for i in range(20):
    Star(all_sprite, star_img)
meteor = Meteor(all_sprite, metero_img)
laser = Laser(all_sprite, laser_img)
spaceship = Spaceship(all_sprite, spaceship_img)






#Main loop
while running:
    dt = clock.tick() / 1000
    #event loop
    for event in pygame.event.get():
        #quitting the game
        if event.type == pygame.QUIT:
            running = False
    
    all_sprite.update(dt)

    #drawing the screen
    screen.fill("darkgray")


    # if key[pygame.K_SPACE]:
    #     print("laser")
    # screen.blit(spaceship,spaceship_rect)
    all_sprite.draw(screen)
    
    pygame.display.update()

pygame.quit()