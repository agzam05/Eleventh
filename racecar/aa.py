import sys,pygame,random,time
from pygame.locals import *
pygame.init()
level=0
coin_sound = pygame.mixer.Sound("coi.mp3")
crash_sound = pygame.mixer.Sound("crash.wav")
ba = pygame.mixer.Sound("background.wav")
HEIGHT,WIDTH=650,350
SPEED=5
SCORE=0
font=pygame.font.SysFont("Verdana", 60)
smallf=pygame.font.SysFont("Verdana", 30)
gameover=font.render("Game Over", True, (0,0,0))
FPS=pygame.time.Clock()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
back=pygame.image.load("road.png")
bac=pygame.transform.scale(back, (WIDTH, HEIGHT))
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imae=pygame.image.load("Enemy.png")
        self.image=pygame.transform.scale(self.imae, (70, 100))
        self.rect=self.image.get_rect()
        self.rect.center = (random.randint(75, WIDTH - 75), -50)
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top>650):
            SCORE+=5
            self.rect.bottom=0
            self.rect.center=(random.randint(75, 300), 0)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imae=pygame.image.load("Player.png")
        self.image=pygame.transform.scale(self.imae, (70, 100))
        self.rect=self.image.get_rect()
        self.rect.center=(175, 600)
    def move(self):
        self.keys=pygame.key.get_pressed()
        if self.keys[K_LEFT] and self.rect.left>0:
            self.rect.move_ip(-5, 0)
        if self.keys[K_RIGHT] and self.rect.right<350:
            self.rect.move_ip(5, 0)
class Point(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.imae=pygame.image.load("coin.png")
        self.x=random.choices([1,2,3,4], weights=[50,30,15,5])[0]
        if self.x==1:
            self.image=pygame.transform.scale(self.imae,(20,20))
            self.rect=self.image.get_rect()
            self.rect.center= (random.randint(20, 330), -20)
        elif self.x==2:
            self.image=pygame.transform.scale(self.imae,(40,40))
            self.rect=self.image.get_rect()
            self.rect.center= (random.randint(40, 310), -40)
        elif self.x==3:
            self.image=pygame.transform.scale(self.imae,(60,60))
            self.rect=self.image.get_rect()
            self.rect.center= (random.randint(60, 290), -60)
        elif self.x==4:
            self.image=pygame.transform.scale(self.imae,(75,75))
            self.rect=self.image.get_rect()
            self.rect.center= (random.randint(75, 275), -75)
    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top>650:
            self.rect.bottom=0
            self.rect.center= (random.randint(30, WIDTH-30), 0)

P1=Player()
E1=Enemy()

enemies=pygame.sprite.Group()
enemies.add(E1)
all_coins=pygame.sprite.Group()

allspc=pygame.sprite.Group()
allspc.add(P1, E1)
all_sprites=pygame.sprite.Group()
all_sprites.add(P1, E1)
ADD_POINTS = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_POINTS, 5000)
running=True
ba.play(-1)
while running:
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
        if event.type == ADD_POINTS:
            if len(all_coins) < 1:  
                C1 = Point()
                all_coins.add(C1)
                all_sprites.add(C1)
    screen.blit(bac, (0,0))
    scores=smallf.render(str(SCORE), True, (255, 255, 255))
    screen.blit(scores, (10,10))
    level=SCORE//50
    if level==1:
        SPEED=7

    elif level==2:
        SPEED=8
    elif level==3:
        SPEED=9
    
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    if pygame.sprite.spritecollideany(P1, all_coins):
        coin_sound.play()
        if C1.x==1:
            SCORE+=5
        elif C1.x==2:
            SCORE+=7
        elif C1.x==3:
            SCORE+=9
        elif C1.x==4:
            SCORE+=11
        pygame.display.update()
        for coin in all_coins:
            coin.kill()
            break
    if pygame.sprite.spritecollideany(P1, enemies):
        ba.stop()
        crash_sound.play()
        screen.fill((255, 0, 0))
        screen.blit(gameover, (5,200))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    pygame.display.update()
    FPS.tick(60)


