
import pygame
import sys
pygame.init()  #pygame初始化
screen = pygame.display.set_mode((500,500))  #窗口
while True:
    pygame.display.update()     #不断绘制画面
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
