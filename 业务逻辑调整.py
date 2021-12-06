
import pygame
import sys
from pygame.locals import *
import time
import random

pygame.init()  #pygame初始化
size = width,height = (400,600)
pygame.display.set_caption("逆行飙车")
screen = pygame.display.set_mode(size)  #窗口
# 定义颜色
BLACK = (0,0,0)
RED = "#ff0000"

SCORE = 0
SPEED = 5  #敌人的运动速度
# 设置图像的帧速率
FPS = 30
clock = pygame.time.Clock()   #返回时钟对象

#定义用户事件
SPEED_UP = pygame.USEREVENT + 1
pygame.time.set_timer(SPEED_UP,1000)

#设置字体和文字
font_big = pygame.font.SysFont("华文仿宋",60)
font_small = pygame.font.SysFont("Verdana",20)
game_over = font_big.render("GAME OVER!",True,BLACK)
# pygame.mixer.Sound('background.wav').play(-1) #loopc参数默认0，-1表示无限次循环

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        x,y = (random.randint(22,378),0)
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((42, 70))  #解决碰撞画面不真实
        self.rect = self.surf.get_rect(center=(x,y))  # (0,0)
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if self.rect.top > height:
            SCORE += 1
            self.rect.top = 0
            self.rect.left = random.randint(22,378)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        x,y=(width/2,height/2)
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((40,75))
        self.rect = self.surf.get_rect(left=178,bottom = height-21)  # (0,0)
    def move(self):
        # self.rect.y -= 1
        # self.rect = self.rect.move(0,-1)
        # self.rect.move_ip(0,-2)
    #键盘事件处理
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP] and self.rect.top >= 0:
            player.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN] and self.rect.bottom <= height-21:
            player.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT] and self.rect.left >= 0 :
            player.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right <= width-4:
            player.rect.move_ip(5, 0)
        # pass


player = Player()
enemy = Enemy()

# 定义精灵组
enemies = pygame.sprite.Group()
enemies.add(enemy)

all_sprite = pygame.sprite.Group()
all_sprite.add(player)
all_sprite.add(enemy)
background = pygame.image.load("AnimatedStreet.png")



while True:
    screen.blit(background, (0, 0))  #绘制局部图像
    scores = font_small.render(str(SCORE),True,BLACK)
    screen.blit(scores,(10,10))
    for sprite in all_sprite:
        screen.blit(sprite.image,sprite.rect)
        sprite.move()
    for event in pygame.event.get():
        # print(event)
        if event.type == SPEED_UP:
            SPEED += 0.5
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 撞击后游戏结束
    if pygame.sprite.spritecollideany(player, enemies):

        # pygame.mixer.Sound("crash.wav").play()
        # time.sleep(1)

        screen.fill(RED)
        screen.blit(game_over,(80,150))

        pygame.display.update()
        time.sleep(2)

        pygame.quit()
        sys.exit()

    pygame.display.update()  # 不断绘制画面
    clock.tick(FPS)  #按照指定的更新速率lock来刷新画面，没到时间就让循环等待
