
import pygame
import sys
from pygame.locals import *
import time
import random

class Constant:
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600
    # 定义颜色
    BLACK = (0, 0, 0)
    RED = "#ff0000"

    SCORE = 0
    SPEED = 5  # 敌人的运动速度
    # 设置图像的帧速率
    FPS = 30




class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        x,y = (random.randint(22,378),0)
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((42, 70))  #解决碰撞画面不真实
        self.rect = self.surf.get_rect(center=(x,y))  # (0,0)
    def move(self):
        # global SCORE
        self.rect.move_ip(0,Constant.SPEED)
        if self.rect.top > Constant.SCREEN_HEIGHT:
            Constant.SCORE += 1
            self.rect.top = 0
            self.rect.left = random.randint(22,378)



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        x,y=(Constant.SCREEN_WIDTH/2,Constant.SCREEN_HEIGHT/2)
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((40,75))
        self.rect = self.surf.get_rect(left=178,bottom = Constant.SCREEN_HEIGHT-21)  # (0,0)
    def move(self):
    #键盘事件处理
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP] and self.rect.top >= 0:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN] and self.rect.bottom <= Constant.SCREEN_HEIGHT-21:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT] and self.rect.left >= 0 :
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right <= Constant.SCREEN_WIDTH-4:
            self.rect.move_ip(5, 0)
        # pass


class Game:
    def __init__(self):
        pygame.init()  # pygame初始化

        # 定义用户事件
        self.SPEED_UP = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPEED_UP, 1000)

        self.clock = pygame.time.Clock()  # 返回时钟对象
        size = width, height = (Constant.SCREEN_WIDTH,Constant.SCREEN_HEIGHT)
        pygame.display.set_caption("逆行飙车")
        self.screen = pygame.display.set_mode(size)  # 窗口
        # 设置字体和文字
        font_big = pygame.font.SysFont("华文仿宋", 60)
        self.font_small = pygame.font.SysFont("Verdana", 20)
        self.game_over = font_big.render("GAME OVER!", True, Constant.BLACK)

    def run(self):
        player = Player()
        enemy = Enemy()

        # 定义精灵组
        enemies = pygame.sprite.Group()
        enemies.add(enemy)

        self.all_sprite = pygame.sprite.Group()
        self.all_sprite.add(player)
        self.all_sprite.add(enemy)

        self.background = pygame.image.load("AnimatedStreet.png")

        pygame.mixer.Sound('background.wav').play(-1) #loopc参数默认0，-1表示无限次循环

        while True:
            self.screen.blit(self.background, (0, 0))  # 绘制局部图像
            scores = self.font_small.render(str(Constant.SCORE), True, Constant.BLACK)
            self.screen.blit(scores, (10, 10))
            for sprite in self.all_sprite:
                self.screen.blit(sprite.image, sprite.rect)
                sprite.move()
            for event in pygame.event.get():
                if event.type == self.SPEED_UP:
                    Constant.SPEED += 0.5
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # 撞击后游戏结束
            if pygame.sprite.spritecollideany(player, enemies):
                pygame.mixer.Sound("crash.wav").play()
                time.sleep(1)

                self.screen.fill(Constant.RED)
                self.screen.blit(self.game_over, (80, 150))

                pygame.display.update()
                time.sleep(2)

                pygame.quit()
                sys.exit()

            pygame.display.update()  # 不断绘制画面
            self.clock.tick(Constant.FPS)  # 按照指定的更新速率lock来刷新画面，没到时间就让循环等待

if __name__=="__main__":
    game = Game()
    game.run()