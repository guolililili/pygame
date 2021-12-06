
import pygame
import sys
from pygame.locals import *
pygame.init()  #pygame初始化
size = width,height = (400,600)
pygame.display.set_caption("逆行飙车")
screen = pygame.display.set_mode(size)  #窗口

# 设置图像的帧速率
FPS = 30
clock = pygame.time.Clock()   #返回时钟对象

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect(left=width/2-24,top=0)  # (0,0)
    def move(self):
       self.rect.move_ip(0,5)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        # super(Player,self).__init__()
        super().__init__()
        x,y=(width/2,height/2)
        self.image = pygame.image.load("Player.png")
        # self.rect = self.image.get_rect(top=200,left=200)  #(0,0)
        self.rect = self.image.get_rect(center=(x,y))  # (0,0)
    def move(self):
        # self.rect.y -= 1
        # self.rect = self.rect.move(0,-1)
        # self.rect.move_ip(0,-2)
    #键盘事件处理
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            player.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            player.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            player.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
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
    for sprite in all_sprite:
        screen.blit(sprite.image,sprite.rect)
        sprite.move()
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 1.敌人和玩家都存在
    # if pygame.sprite.spritecollide(player,enemies,False):
    #     print("撞车了")
    # 2.敌人消失
    # if pygame.sprite.spritecollide(player,enemies,True):
    #     print("撞车了")
    # 3.敌人和玩家都消失
    # if pygame.sprite.spritecollide(player,enemies,True):
    #     player.kill()  #单独控制某个精灵消失
    #     print("撞车了")
    # 4.玩家消失
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()  # 单独控制某个精灵消失
        print("撞车了")
    if player not in all_sprite:
        all_sprite.add(player)



    pygame.display.update()  # 不断绘制画面
    clock.tick(FPS)  #按照指定的更新速率lock来刷新画面，没到时间就让循环等待
