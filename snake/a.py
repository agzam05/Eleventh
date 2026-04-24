import pygame, sys, time, random
from pygame.locals import *
pygame.init()
WIDTH,HEIGHT=500, 500
SPEED,SCORE, OCK=10,0, 10

screen=pygame.display.set_mode((WIDTH, HEIGHT))
imge=pygame.image.load("pitch.png")
font=pygame.font.SysFont("Verdana", 30)
image=pygame.transform.scale(imge, (500,500))
FPS=pygame.time.Clock()
running=True
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imae=pygame.image.load("apple.png")
        self.image=pygame.transform.scale(self.imae, (20,20))
        self.rect=self.image.get_rect()
    def randoming(self):
        self.rect.center=(random.randint(0, WIDTH // 10 - 1) * 10,
        random.randint(0, HEIGHT // 10 - 1) * 10)
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.snake_body=[(100,100), (90,100), (80,100)]
        self.image=pygame.Surface((10,10))
        self.rect=self.image.get_rect()
        self.rect.center=(100, 100)
    def move(self):
        self.headx, self.heady=self.snake_body[0]
        self.keys=pygame.key.get_pressed()
        if self.keys[K_LEFT] and  self.headx>0:
            self.headx-=SPEED
            new_head=(self.headx, self.heady)
            self.snake_body.insert(0, new_head)
            self.snake_body.pop()
        elif self.keys[K_RIGHT] and self.headx<WIDTH-10:
            self.headx+=SPEED
            new_head=(self.headx, self.heady)
            self.snake_body.insert(0, new_head)
            self.snake_body.pop()
        elif self.keys[K_UP] and self.heady>0:
            self.heady-=SPEED
            new_head=(self.headx, self.heady)
            self.snake_body.insert(0, new_head)
            self.snake_body.pop()
        elif self.keys[K_DOWN] and self.heady<HEIGHT-10:
            self.heady+=SPEED
            new_head=(self.headx, self.heady)
            self.snake_body.insert(0, new_head)
            self.snake_body.pop()
        elif self.heady<=0 or self.heady>=HEIGHT-10 or self.headx<=0 or self.headx>=WIDTH-10:
            pygame.quit()
            sys.exit()
A1=Food()
S1=Snake()

while running:
    scor=font.render(str(SCORE), True, (0,0,0))
    leve=font.render(str(SCORE//15), True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
    
    screen.blit(image, (0,0))
    screen.blit(A1.image, A1.rect)
    screen.blit(scor, (5,10))
    screen.blit(leve, (480,10))
    S1.move()
    if S1.snake_body[0]==A1.rect.center:
        A1.randoming() 
        SCORE+=5
        if OCK<30:
            if SCORE%15==0:
                OCK+=2
        
    for blovk in S1.snake_body:
        pygame.draw.rect(screen, (0,0,0), (*blovk, 10, 10))
    pygame.display.update()
    FPS.tick(OCK)
pygame.quit()
sys.exit()