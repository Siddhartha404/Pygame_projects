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
spaceship = pygame.image.load('images/spaceship.png').convert_alpha()
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
    screen.blit(spaceship,(100,200))
    pygame.display.update()

pygame.quit()