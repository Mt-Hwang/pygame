# 선 그리기

import pygame

pygame.init()

screen = pygame.display.set_mode((480, 360))

pygame.display.set_caption("선 그리기!")

running = True

def runGame() :
    global running
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

        screen.fill((255, 255, 255))
        
        pygame.draw.line(screen, (0, 0, 0), (240,0), (240, 360), 10)
        pygame.draw.line(screen, (0, 0, 0), (0, 180), (480, 180), 10)
        pygame.draw.line(screen, (0, 0, 0), (0,0), (480, 360), 10)
        pygame.draw.line(screen, (0, 0, 0), (0, 360), (480, 0), 10)
        
        pygame.display.update()

    pygame.quit()

runGame()


# for문으로 선 그리기

import pygame

pygame.init()

screen = pygame.display.set_mode((480, 360))

pygame.display.set_caption("for문으로 선 그리기!")

running = True

def runGame() :
    global running
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

        screen.fill((255, 255, 255))

        for i in range(0, 480, 30) :
            pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 360))

        for i in range(0, 360, 30) :
            pygame.draw.line(screen, (0, 0, 0), (0, i), (480, i))
            
        pygame.display.update()

    pygame.quit()

runGame()


# 원 그리기

import pygame

pygame.init()

screen = pygame.display.set_mode((480, 360))

pygame.display.set_caption("원 그리기!")

x = screen.get_size()[0]//2
y = screen.get_size()[1]//2

running = True

def runGame() :
    global running, x, y
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

        screen.fill((255, 255, 255))

        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, 360))
        pygame.draw.line(screen, (0, 0, 0), (0, y), (480, y))

        pygame.draw.circle(screen, (255, 0, 0), (x, y),  50, 5)
        
        pygame.display.update()

    pygame.quit()

runGame()


# 사각형 그리기1

import pygame

pygame.init()

screen = pygame.display.set_mode((480, 360))

pygame.display.set_caption("사각형 그리기1!")

x = screen.get_size()[0]//2
y = screen.get_size()[1]//2

running = True

def runGame() :
    global running, x, y
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

        screen.fill((255, 255, 255))

        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, 360))
        pygame.draw.line(screen, (0, 0, 0), (0, y), (480, y))

        pygame.draw.rect(screen, (0, 255, 0), (x, y, 100, 50))
        
        pygame.display.update()

    pygame.quit()

runGame()


# 사각형 그리기2

import pygame

pygame.init()

screen = pygame.display.set_mode((480, 360))

pygame.display.set_caption("사각형 그리기2!")

x = screen.get_size()[0]//2
y = screen.get_size()[1]//2

running = True

def runGame() :
    global running, x, y
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

        screen.fill((255, 255, 255))

        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, 360))
        pygame.draw.line(screen, (0, 0, 0), (0, y), (480, y))

        pygame.draw.rect(screen, (0, 255, 0), (x-50, y-25, 100, 50), 5)
        pygame.draw.rect(screen, (0, 255, 0), (x, y, 100, 50), 5)
        
        pygame.display.update()

    pygame.quit()

runGame()


# 타원 그리기1

import pygame

pygame.init()

screen = pygame.display.set_mode((480, 360))

pygame.display.set_caption("타원 그리기1!")

x = screen.get_size()[0]//2
y = screen.get_size()[1]//2

running = True

def runGame() :
    global running, x, y
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

        screen.fill((255, 255, 255))

        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, 360))
        pygame.draw.line(screen, (0, 0, 0), (0, y), (480, y))

        pygame.draw.ellipse(screen, (0, 0, 255), (x, y, 100, 50))
        
        pygame.display.update()

    pygame.quit()

runGame()


# 타원 그리기2

import pygame

pygame.init()

screen = pygame.display.set_mode((480, 360))

pygame.display.set_caption("타원 그리기2!")

x = screen.get_size()[0]//2
y = screen.get_size()[1]//2

running = True

def runGame() :
    global running, x, y
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

        screen.fill((255, 255, 255))

        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, 360))
        pygame.draw.line(screen, (0, 0, 0), (0, y), (480, y))

        pygame.draw.ellipse(screen, (0, 0, 255), (x-50, y-25, 100, 50), 5)
        pygame.draw.ellipse(screen, (0, 0, 255), (x, y, 100, 50), 5)
        
        pygame.display.update()

    pygame.quit()

runGame()


# 다각형 그리기

import pygame

pygame.init()

screen = pygame.display.set_mode((480, 360))

pygame.display.set_caption("다각형 그리기!")

x = screen.get_size()[0]//2
y = screen.get_size()[1]//2

running = True

def runGame() :
    global running, x, y
    
    while running :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                running = False

        screen.fill((255, 255, 255))

        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, 360))
        pygame.draw.line(screen, (0, 0, 0), (0, y), (480, y))

        pygame.draw.polygon(screen, (255, 255, 0), ((0, 0), (80, 200), (160, 260), (400, 20)), 5)
                            
        pygame.display.update()

    pygame.quit()

runGame()

