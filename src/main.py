# -*- coding:utf-8 -*-

# 参考サイト
# https://algorithm.joho.info/programming/python/pygame/

import sys
import time
import random

import pygame
from pygame.locals import *


window_size = (300, 600)


def main():
    pygame.init()# Pygameの初期化
    screen = pygame.display.set_mode(window_size) # 400*300の画面
    pygame.display.set_caption("Test")            # タイトルバーに表示する文字
    x0 = 10
    y0 = 10
    x1 = 20
    y1 = 20
    score = 0

    rect = Rect(x0, y0, x1, y1)
    stage = Rect(10,10,window_size[0] - 20, window_size[1] - 20)
    back_ground_image = pygame.image.load(r".\..\resource\back_ground.png").convert_alpha()
    back_ground = back_ground_image.get_rect()
    basket_image = pygame.image.load(r".\..\resource\basket.png").convert_alpha()
    basket = basket_image.get_rect()
    basket.center = (window_size[0] / 2, window_size[1] - (basket.bottom - basket.top))

    font = pygame.font.SysFont("hg正楷書体pro", 20)
    
    
    while (1):
        screen.fill((0,0,0))        # 画面を黒色(#000000)に塗りつぶし
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            basket.move_ip(-1,0)
        if pressed_key[K_RIGHT]:
            basket.move_ip(1, 0)
        if pressed_key[K_DOWN]:
            rect.move_ip(random.randrange(window_size[0]), -window_size[1] - rect.top)
            
        rect.move_ip(0,1)
        screen.blit(back_ground_image, back_ground)

        pygame.draw.rect(screen, (0, 80, 0), rect)
        pygame.draw.rect(screen, (255, 255, 255), stage, 5)

        screen.blit(basket_image, basket)
        

        score_text = font.render("SCORE:{0}".format(score), True, (0, 0, 0))
        screen.blit(score_text, (200, 10))
        
        pygame.display.update()  # 画面を更新

        if basket.left <= rect.left and basket.right >= rect.right:
            if basket.top + 5 <= rect.bottom and basket.top + 5 >= rect.top:
                rect.move_ip((random.randrange(0,window_size[0]) - rect.right),- rect.top)
                print("get!!")
                score = score + 1
                print(score)

        if rect.bottom == window_size[1]:
            rect.move_ip((random.randrange(0, window_size[0]) - rect.right), -rect.top)

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()

        time.sleep(0.01)

if __name__ == "__main__":
    main()
