import pygame
import pygame.display
from random import randint
#initializing
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")
running = True

#surface

#saceship
spaceship = pygame.image.load('images/spaceship.png').convert_alpha()
spaceship_rect = spaceship.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT-50))
direction = 1

#Meteor
meteor = pygame.image.load('images/meteor.png').convert_alpha()
meteor_rect = meteor.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

#laser
laser = pygame.image.load('images/laser.png').convert_alpha()
laser_rect = meteor.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))

#all the stars
star = pygame.image.load('images/star.png').convert_alpha()
positions = [(randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT)) for i in range(20)]
#Main loop
while running:
    #event loop
    for event in pygame.event.get():
        #quitting the game
        if event.type == pygame.QUIT:
            running = False
    screen.fill("darkgray")
    
    for position in positions:
        screen.blit(star,position)


    screen.blit(meteor,meteor_rect)
    screen.blit(laser,laser_rect)

    #spaceship movement
    spaceship_rect.x += direction * 0.2
    if spaceship_rect.right > WINDOW_WIDTH or spaceship_rect.left < 0:
        direction *= -1
    screen.blit(spaceship,spaceship_rect)
    
    
    pygame.display.update()

pygame.quit()