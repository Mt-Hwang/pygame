# 마우스로 조종하기

import pygame

pygame.init()

screen = pygame.display.set_mode((480, 640))

pygame.display.set_caption("마우스로 조종하기!")

running = True

def runGame() :
    global running
 
    while running :

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

            if event.type == pygame.MOUSEMOTION :
                print("MOUSEMOTION")
                print(pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONDOWN :
                print("MOUSEBUTTONDOWN")
            if event.type == pygame.MOUSEBUTTONUP :
                print("MOUSEBUTTONUP")        

    pygame.display.update()

    pygame.quit()

runGame()


# 마우스 버튼 좌표 출력

import pygame

pygame.init()

screen = pygame.display.set_mode((480, 640))

pygame.display.set_caption("마우스 버튼 좌표 출력!")

running = True

def runGame() :
    global running
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN :
                print("현재 마우스의 좌표는..!")
                print(pygame.mouse.get_pos())
                
        pygame.display.update()

    pygame.quit()

runGame()


# 이벤트 버튼 확인

import pygame

pygame.init()

screen = pygame.display.set_mode((480, 640))

pygame.display.set_caption("이벤트 버튼 확인!")

running = True

def runGame() :
    global running
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 1 :
                    print("마우스 왼쪽을 클릭하셨네요.")
                elif event.button == 2 :
                    print("마우스 휠을 클릭하셨네요.")
                elif event.button == 3 :
                    print("마우스 오른쪽을 클릭하셨네요.")
                elif event.button == 4 :
                    print("마우스 휠을 올리셨네요.")
                elif event.button == 5 :
                    print("마우스 휠을 내리셨네요.")
        pygame.display.update()

    pygame.quit()

runGame()


# 마우스로 그리기

import pygame

pygame.init()

screen = pygame.display.set_mode((480, 640))

pygame.display.set_caption("마우스로 그리기!")

running = True

circle_xy = []

def runGame() :
    global running, circle_xy
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

            if event.type == pygame.MOUSEMOTION :
                circle_xy = list(pygame.mouse.get_pos())
                pygame.draw.circle(screen, (0, 0, 255), (circle_xy[0], circle_xy[1]), 10)

        pygame.display.update()

    pygame.quit()

runGame()


# 마우스 포인트

import pygame

pygame.init()

screen = pygame.display.set_mode((480, 640))

pygame.display.set_caption("마우스 포인트!")

running = True

x = screen.get_size()[0]//2
y = screen.get_size()[1]//2


def runGame() :
    global running, x, y
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN :
                x, y = pygame.mouse.get_pos()

        screen.fill((255, 255, 255))

        pygame.draw.circle(screen, (0, 0, 255), (x, y), 10)
        
        pygame.display.update()

    pygame.quit()

runGame()

