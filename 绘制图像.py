
import pygame
import sys
pygame.init()  #pygame初始化
size = width,height = (400,600)
pygame.display.set_caption("绘制图像")
screen = pygame.display.set_mode(size)  #窗口

# 设置图像的帧速率
FPS = 30
clock = pygame.time.Clock()   #返回时钟对象


background = pygame.image.load("AnimatedStreet.png")
player = pygame.image.load("Player.png")
x,y = 178,504


while True:
    screen.blit(background, (0, 0))  #绘制局部图像
    screen.blit(player,(x,y))
    y -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()  # 不断绘制画面
    clock.tick(FPS)  #按照指定的更新速率lock来刷新画面，没到时间就让循环等待
