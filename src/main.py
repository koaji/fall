# -*- coding:utf-8 -*-

# 参考サイト
# https://algorithm.joho.info/programming/python/pygame/

import sys
import time
import random

import pygame
from pygame.locals import *


window_size = (300, 600)

class Drops:
    def __init__(self, image_number, position):
        self.image_num = image_number
        self.pos = position

def main():
    pygame.init()# Pygameの初期化
    screen = pygame.display.set_mode(window_size) # 400*300の画面
    pygame.display.set_caption("Test")            # タイトルバーに表示する文字
    score = 0

    stage = Rect(10, 10, window_size[0] - 20, window_size[1] - 20)

    drops_list = []
    drops_image = pygame.image.load(r".\..\resource\drops.png").convert_alpha()
    for i in range(0, 3):
        temp = pygame.Surface((20,20))
        temp.blit(drops_image, (0, 0), (i * 20, 0, 20, 20))
        # なぜかアルファチャンネルが効かないので，透過色キーを設定して，透過処理
        #temp = pygame.transform.scale(temp, (40, 40))
        temp.set_colorkey(temp.get_at((0,0)), RLEACCEL)
        drops_list.append(temp)
    
    # アイテム生成
    drops = []
    for i in range(0, 10):
        image_num = random.randrange(0,3)
        temp = Drops(image_num, drops_list[image_num].get_rect())
        # アイテム位置を初期化
        temp.pos.move_ip((random.randrange(0, window_size[0]) - temp.pos.right), -temp.pos.top)
        drops.append(temp)

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
            if basket.left > 0 :
                basket.move_ip(-1,0)
        if pressed_key[K_RIGHT]:
            if basket.right <= window_size[0] :
                basket.move_ip(1, 0)
        
        screen.blit(back_ground_image, back_ground)
        pygame.draw.rect(screen, (255, 255, 255), stage, 5)
        screen.blit(basket_image, basket)

        score_text = font.render("SCORE:{0}".format(score), True, (0, 0, 0))
        screen.blit(score_text, (180, 10))

        for i in range(0, 10):
            
            # アイテムを描画
            screen.blit(drops_list[drops[i].image_num], drops[i].pos)
            
            # キャッチ判定
            if basket.left <= drops[i].pos.left and basket.right >= drops[i].pos.right:
                if basket.top + 5 <= drops[i].pos.bottom and basket.top + 5 >= drops[i].pos.top:
                    drops[i].pos.move_ip((random.randrange(0,window_size[0]) - drops[i].pos.right),- drops[i].pos.top)
                    print("get!!")
                    score = score + 1
                    print(score)
                    # アイテムのランダム変更
                    drops[i].image_num = random.randrange(0,3)

            if drops[i].pos.bottom == window_size[1]:
                drops[i].pos.move_ip((random.randrange(0, window_size[0]) - drops[i].pos.right), -drops[i].pos.top)
            
            # すべての落ち物の落下移動
            drops[i].pos.move_ip(0, 1)
            

        pygame.display.update()  # 画面を更新

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()

        time.sleep(0.01)

if __name__ == "__main__":
    main()
