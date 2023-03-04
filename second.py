import pygame,sys
import random
import time


pygame.init()
Clock = pygame.time.Clock()
FPS = 60
size = [1000,800]
bg = [0,0,0]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('MyGame')


class Player:
    def __init__(self,vel,x,y):
        self.vel = vel
        self.vel_y = 16
        self.x = x
        self.y = y
        self.jump = False

    def move(self):
        k = pygame.key.get_pressed()
        if k[pygame.K_LEFT]:
            self.x -= self.vel
        if k[pygame.K_RIGHT]:
            self.x += self.vel
        if k[pygame.K_UP] and self.vel_y == 16:
            self.jump = True
        if self.jump:
            pass
            if self.vel_y >= -16:
                self.y -= self.vel_y
                self.vel_y -= 1
            else:
                self.jump = False
                self.vel_y = 16

    def draw(self):
        self.player_ = pygame.draw.rect(screen,(255,255,255),(self.x,self.y,50,100))

    def do(self):
        self.move()
        self.draw()
        


class Enemy:
    def __init__(self, x, y, vel_y):
        self.x = x
        self.y = y
        self.vel_y = vel_y

    def draw(self):
        self.enemy_ = pygame.draw.rect(screen,(255,255,255),(self.x,self.y,50,50))
        self.y += 2

    

class Border:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        self.border_ = pygame.draw.line(screen, (255,255,255), (self.x1, self.y1), (self.x2, self.y2), 10)




player = Player(5,500,600)
enemy = Enemy(random.randint(0, 1000), 0, 10)
border = Border(0,700,1000,700)
running = True


def check_collision(enemy, player):
    if pygame.rect.colliderect(enemy, player) = True:
        enemy.de

while running:
    
    screen.fill(bg)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
     
    player.do()
    enemy.draw()
    border.draw()

    #if enemy.y == 800:
    enemy.draw()

    #if player.player_.colliderect(enemy.enemy_):
      


    Clock.tick(FPS)
    pygame.display.update()