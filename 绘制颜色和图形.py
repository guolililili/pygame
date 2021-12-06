
import pygame
import sys
pygame.init()  #pygame初始化
pygame.display.set_caption("绘制图形")
size = width,height = 300,300
screen = pygame.display.set_mode(size)  #窗口
# 颜色常量
WHITE = pygame.color.Color(255,255,255)
BLACK = pygame.color.Color(0,0,0,a=255)
RED = '#ff0000'
GREEN = '0x00FF00'
BLUE = (0,0,255)
screen.fill(WHITE)
while True:
    pygame.draw.circle(screen,BLACK,(100,50),30) #在(100,50)坐标处绘制半径为30px的圆形
    pygame.draw.circle(screen, BLACK, (200, 50), 30,3,False,False,True,True)  # 在(200,50)坐标处绘制半径为30px的圆形
    pygame.draw.line(screen, BLUE, (150, 130),(130, 170)) # 画一条蓝色，以(150, 130)为起点,(130, 170)为终点的线条
    pygame.draw.line(screen, BLUE, (150, 130), (170, 170),1)
    pygame.draw.line(screen, GREEN, (130, 170), (170, 170),5)
    pygame.draw.rect(screen,RED,(100,200,100,50),2) # 画矩形
    pygame.draw.rect(screen, BLACK, (110, 260, 80, 5))  # 画矩形
    pygame.display.update()     #不断绘制画面
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
