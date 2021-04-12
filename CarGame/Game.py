#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initializing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GOLD = (255, 215, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
SCOREc = 0

#For moving road
background1 = pygame.image.load("AnimatedStreet.png")
background2 = pygame.image.load("AnimatedStreet.png")
y1 = 0
y2 = -600

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 


#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        global enemy_coordinate
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((42, 70))
        self.coordinate = random.randint(40, SCREEN_WIDTH - 40)
        while (self.coordinate < C1.coordinate + 33 and self.coordinate > C1.coordinate - 33):
          self.coordinate = random.randint(40, SCREEN_WIDTH - 40)
        self.rect = self.surf.get_rect(center = (self.coordinate, 0))
 
      def move(self):
        global SCORE
        global SPEED
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SPEED = random.randint(2, 5)
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
class Coin(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Coin.png")
        self.surf = pygame.Surface((24, 24))
        self.coordinate = random.randint(40, SCREEN_WIDTH - 40)
        try:
          while (self.coordinate < E1.coordinate + 33 and self.coordinate > E1.coordinate - 33):
            self.coordinate = random.randint(40, SCREEN_WIDTH - 40)
        except Exception:
          pass
        self.rect = self.surf.get_rect(center = (self.coordinate, 0))
        
 
      def move(self):
        global SCOREc
        self.rect.move_ip(0, 1)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center = (160, 520))
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                   
#Setting up Sprites        
P1 = Player()
C1 = Coin()
E1 = Enemy()


#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(C1)
all_sprites.add(E1) 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get(): 
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    

    DISPLAYSURF.blit(background1, (0, y1))
    DISPLAYSURF.blit(background1, (0, y2))

    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    
    scoresc = font_small.render(str(SCOREc), True, GOLD)
    DISPLAYSURF.blit(scoresc, (375 ,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    #Picks up a coin
    if pygame.sprite.spritecollideany(P1, coins):
          #pygame.mixer.Sound('add_coin.wav').play()
          SCOREc += 1         
          C1.rect.center = (0 , 650)
    
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()
    
    y1 += 1
    if y1 > 600:
      y1 = -599
    y2 += 1
    if y2 > 600:
      y2 = - 599
    pygame.display.update()
    FramePerSec.tick(FPS)

