import pygame
import pygame.display
from random import randint, uniform


#initializing
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")
running = True
clock = pygame.time.Clock()
SCORE = 0

#saceship
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, groups, img):
        super().__init__(groups)
        self.image = img
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT-50))
        self.direction = pygame.math.Vector2(1,1)
        self.speed = 400

        #laser cooldown
        self.can_shoot = True
        self.shoot_time = 0
        self.cooldown = 300

        #mask
        self.mask = pygame.mask.from_surface(self.image)


    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.cooldown:
                self.can_shoot = True

    def update(self, dt):
        #spaceship movement
        key = pygame.key.get_pressed()
        self.direction.x = int(key[pygame.K_RIGHT]) - int(key[pygame.K_LEFT])
        self.direction.y = int(key[pygame.K_DOWN]) - int(key[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        #logic for lager
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            laser_pos = self.rect.midtop
            Laser((all_sprite,laser_sprites), laser_img, laser_pos )
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()
        self.laser_timer()
#star
class Star(pygame.sprite.Sprite):
    def __init__(self, groups, img):
        super().__init__(groups)   
        self.image = img
        self.rect = self.image.get_frect(center=((randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT))))
        #mask
        self.mask = pygame.mask.from_surface(self.image)
#meteor 
class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups, img):
        super().__init__(groups)   
        self.image = img
        self.rect = self.image.get_frect(center=((randint(0,WINDOW_WIDTH),randint(-200,-100))))
        self.create_time = pygame.time.get_ticks()
        self.speed = randint(400,500)
        self.direction = pygame.Vector2(uniform(-0.5,0.5),1)

        #mask
        self.mask = pygame.mask.from_surface(self.image)
    def update(self, dt):
        current_time = pygame.time.get_ticks()
        self.rect.center += self.direction * self.speed * dt
        if current_time - self.create_time >= 3000:
            self.kill()
#laser
class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, img, pos):
        super().__init__(groups)   
        self.image = img
        self.rect = self.image.get_frect(midbottom = pos)
        self.speed = 400

        #mask
        self.mask = pygame.mask.from_surface(self.image)
    def update(self,dt):
        self.rect.y -= self.speed * dt
        if self.rect.bottom < 0:
            self.kill()

#scoring function
def game_score():
    text = font.render(str(SCORE), True, 'white')
    text_rect = text.get_frect(midbottom = (WINDOW_WIDTH /2, WINDOW_HEIGHT - 50))
    screen.blit(text,text_rect)
    pygame.draw.rect(screen, 'white', text_rect.inflate(20,20).move(0,-4), 5,10)

#all imports
spaceship_img = pygame.image.load('images/spaceship.png').convert_alpha()
star_img = pygame.image.load('images/star.png').convert_alpha()
metero_img = pygame.image.load('images/meteor.png').convert_alpha()
laser_img = pygame.image.load('images/laser.png').convert_alpha()

#importing fonts
font = pygame.font.Font(None, 40)

#for sprites
all_sprite = pygame.sprite.Group()
Meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
for i in range(20):
    Star(all_sprite, star_img)

spaceship = Spaceship(all_sprite, spaceship_img)

#custom events
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

#check for collision
def collision():
    global SCORE
    global running
    collision_sprites = pygame.sprite.spritecollide(spaceship, Meteor_sprites, True, pygame.sprite.collide_mask)
    if collision_sprites:
        running = False
        
    for laser in laser_sprites:
        collisions = pygame.sprite.spritecollide(laser, Meteor_sprites, True)
        if collisions:
            SCORE += 10
            laser.kill()
            
#Main loop
while running:
    dt = clock.tick() / 1000
    #event loop
    for event in pygame.event.get():
        #quitting the game
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            Meteor((Meteor_sprites,all_sprite), metero_img)
        
    all_sprite.update(dt)
    collision()
    #drawing the screen
    screen.fill("#3a2e3f")
    game_score()
    all_sprite.draw(screen)
    pygame.display.update()

pygame.quit()