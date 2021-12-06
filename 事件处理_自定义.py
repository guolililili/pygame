
import pygame
import sys
from pygame.locals import *
pygame.init()  #pygame初始化
size = width,height = (400,600)
pygame.display.set_caption("绘制图像")
screen = pygame.display.set_mode(size)  #窗口

# 设置图像的帧速率
FPS = 30
clock = pygame.time.Clock()   #返回时钟对象

#-定义用户事件类型及编码

#定义用户事件触发条件
#定义用户事件处理过程

#-定义用户事件
OUT_OF_RANGE = pygame.USEREVENT + 1


class Player:
    def __init__(self):
        x,y=(width/2,height/2)
        self.image = pygame.image.load("Player.png")
        # self.rect = self.image.get_rect(top=200,left=200)  #(0,0)
        self.rect = self.image.get_rect(center=(x,y))  # (0,0)
    def move(self):
        # self.rect.y -= 1
        # self.rect = self.rect.move(0,-1)
        # self.rect.move_ip(0,-2)
        #
        if self.rect.left < 40 or self.rect.right > 360:
            pygame.event.post(pygame.event.Event(OUT_OF_RANGE))

        #键盘事件处理
        # pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[pygame.K_UP]:
        #     player.rect.move_ip(0, -5)
        # if pressed_keys[pygame.K_DOWN]:
        #     player.rect.move_ip(0, 5)
        # if pressed_keys[K_LEFT]:
        #     player.rect.move_ip(-5, 0)
        # if pressed_keys[K_RIGHT]:
        #     player.rect.move_ip(5, 0)
        #鼠标时间处理
        mouseX,mouseY = pygame.mouse.get_pos()
        # if 22 <= mouseX <= width-22 and 48 <= mouseY <= height-48:
        if player.rect.width/2 <= mouseX <= width - player.rect.width/2 \
                and player.rect.height/2 <= mouseY <= height - player.rect.height/2:
            player.rect.center = (mouseX,mouseY)
        # player.rect.x = mouseX
        # player.rect.y = mouseY
        # pass


player = Player()

background = pygame.image.load("AnimatedStreet.png")
# player = pygame.image.load("Player.png")
# x,y = 178,504


while True:
    screen.blit(background, (0, 0))  #绘制局部图像
    screen.blit(player.image,player.rect)
    # y -= 1
    player.move()
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #对用户自定义事件处理
        if event.type == OUT_OF_RANGE:
            print("越界")
    # #     键盘事件处理
    # pressed_keys = pygame.key.get_pressed()
    # if pressed_keys[pygame.K_DOWN]:
    #     player.rect.move_ip(0,5)


    pygame.display.update()  # 不断绘制画面
    clock.tick(FPS)  #按照指定的更新速率lock来刷新画面，没到时间就让循环等待
