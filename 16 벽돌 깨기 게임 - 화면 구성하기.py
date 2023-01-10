# 벽돌 깨기 게임 - 화면 구성하기

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((480, 360))

pygame.display.set_caption("벽돌 깨기 게임 - 화면 구성하기!")


# 배경 사이즈
screen_l = screen.get_size()[0]
screen_h = screen.get_size()[1]


# 페달 사이즈, 좌표, 사각화
pedal_l = 100
pedal_h = 15

pedal_x = screen_l//2 - pedal_l//2
pedal_y = screen_h//2 - pedal_h//2

pedal_rect = pygame.Rect(pedal_x, pedal_y, pedal_l, pedal_h)


# 공의 사이즈, 좌표, 사각화
ball_size = 20

ball_x = screen_l//2
ball_y = screen_h - pedal_h - ball_size

ball_rect = pygame.Rect(ball_x, ball_y, ball_size*2, ball_size*2)
ball_rect.center = (ball_x, ball_y)


# 블록 사이즈, 좌표, 사각화
block_l = screen_l//10
block_h = 30

block_x = 0
block_y = 0

block_rect = [[] for _ in range(10)]
block_color = [[] for _ in range(10)]

for i in range(10) :
    for j in range(3) :
        block_rect[i].append(pygame.Rect(i*block_l, j*block_h, block_l, block_h))
        block_color[i].append((random.randrange(255), random.randrange(150, 255), random.randrange(150, 255)))
                              
             
running = True

def runGame() :
    global running
    global pedal_x, pedal_y, pedal_l, pedal_h
    global ball_x, ball_y
    global block_l, block_y, block_rect, block_color
    global block_rect, block_color
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

        screen.fill((255, 255, 255))

        pygame.draw.rect(screen, (255, 255, 0), (0, 50, 150, 100))

        pygame.draw.circle(screen, (255, 0, 255), (200, 200), 30)

        # 블록 그리기
        for i in range(10) :
            for j in range(3) :
                if block_rect[i][j] :
                    pygame.draw.rect(screen, block_color[i][j], block_rect[i][j])
                    block_rect[i][j].topleft = (i*block_l, j*block_h)
                
        pygame.display.update()

    pygame.quit()

runGame()

